#!/bin/bash
# ============================================
# install-cron.sh - Quick Cron Installation Script
# ============================================
# What? Automated installation of autocommit cron job
# For? Simplify the setup process for Fedora 42
# Impact? One-command installation with validation
# ============================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Repository path - will be auto-detected
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_PATH="$(dirname "$SCRIPT_DIR")"
AUTOCOMMIT_SCRIPT="$SCRIPT_DIR/auto-commit.sh"
CRON_INTERVAL="${1:-5}"  # Default to 5 minutes if not specified

# Function to print colored messages
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "\n${BLUE}================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================${NC}\n"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main installation process
main() {
    print_header "Autocommit Cron Installation"
    
    # Step 1: Verify we're in a git repository
    print_info "Checking if we're in a git repository..."
    if [ ! -d "$REPO_PATH/.git" ]; then
        print_error "Not a git repository: $REPO_PATH"
        print_info "Please run this script from within the bootcamp repository"
        exit 1
    fi
    print_success "Git repository found: $REPO_PATH"
    
    # Step 2: Check if git is installed
    print_info "Checking if git is installed..."
    if ! command_exists git; then
        print_error "Git is not installed"
        print_info "Install it with: sudo dnf install git -y"
        exit 1
    fi
    print_success "Git is installed"
    
    # Step 3: Check git configuration
    print_info "Checking git configuration..."
    GIT_USER=$(git config --global user.name 2>/dev/null || echo "")
    GIT_EMAIL=$(git config --global user.email 2>/dev/null || echo "")
    
    if [ -z "$GIT_USER" ] || [ -z "$GIT_EMAIL" ]; then
        print_warning "Git user not configured"
        print_info "Please configure git:"
        echo "  git config --global user.name \"Your Name\""
        echo "  git config --global user.email \"your.email@example.com\""
        exit 1
    fi
    print_success "Git configured: $GIT_USER <$GIT_EMAIL>"
    
    # Step 4: Check if crond is installed and running
    print_info "Checking crond service..."
    if ! systemctl is-active --quiet crond; then
        print_warning "Crond is not running"
        print_info "Starting crond service..."
        if sudo systemctl enable --now crond; then
            print_success "Crond service started and enabled"
        else
            print_error "Failed to start crond service"
            exit 1
        fi
    else
        print_success "Crond is running"
    fi
    
    # Step 5: Update REPO_PATH in auto-commit.sh
    print_info "Updating repository path in auto-commit.sh..."
    if [ -f "$AUTOCOMMIT_SCRIPT" ]; then
        # Create backup
        cp "$AUTOCOMMIT_SCRIPT" "$AUTOCOMMIT_SCRIPT.backup"
        
        # Update REPO_PATH
        sed -i "s|^REPO_PATH=.*|REPO_PATH=\"$REPO_PATH\"|" "$AUTOCOMMIT_SCRIPT"
        print_success "Repository path updated in script"
    else
        print_error "auto-commit.sh not found at: $AUTOCOMMIT_SCRIPT"
        exit 1
    fi
    
    # Step 6: Make script executable
    print_info "Making auto-commit.sh executable..."
    chmod +x "$AUTOCOMMIT_SCRIPT"
    print_success "Script is now executable"
    
    # Step 7: Test the script
    print_info "Testing auto-commit script..."
    if bash "$AUTOCOMMIT_SCRIPT"; then
        print_success "Script test successful"
    else
        print_warning "Script test completed (check logs for details)"
    fi
    
    # Step 8: Check if cron job already exists
    print_info "Checking for existing cron job..."
    if crontab -l 2>/dev/null | grep -q "auto-commit.sh"; then
        print_warning "Cron job already exists"
        print_info "Current cron jobs:"
        crontab -l | grep "auto-commit.sh"
        
        read -p "Do you want to replace it? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "Installation cancelled"
            exit 0
        fi
        
        # Remove old cron job
        crontab -l | grep -v "auto-commit.sh" | crontab -
        print_success "Old cron job removed"
    fi
    
    # Step 9: Install cron job
    print_info "Installing cron job (runs every $CRON_INTERVAL minutes)..."
    
    CRON_JOB="*/$CRON_INTERVAL * * * * $AUTOCOMMIT_SCRIPT >> $REPO_PATH/.autocommit.log 2>&1"
    
    # Add to crontab
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    
    if [ $? -eq 0 ]; then
        print_success "Cron job installed successfully"
    else
        print_error "Failed to install cron job"
        exit 1
    fi
    
    # Step 10: Verify installation
    print_header "Installation Summary"
    
    echo "📁 Repository: $REPO_PATH"
    echo "📝 Script: $AUTOCOMMIT_SCRIPT"
    echo "⏰ Interval: Every $CRON_INTERVAL minutes"
    echo "📄 Log file: $REPO_PATH/.autocommit.log"
    echo ""
    echo "Current cron job:"
    echo "  $CRON_JOB"
    echo ""
    
    print_success "Installation completed!"
    
    print_header "Next Steps"
    
    echo "1. Monitor the log file:"
    echo "   tail -f $REPO_PATH/.autocommit.log"
    echo ""
    echo "2. View cron jobs:"
    echo "   crontab -l"
    echo ""
    echo "3. Check git commits:"
    echo "   git log --oneline -10"
    echo ""
    echo "4. To uninstall, run:"
    echo "   crontab -e"
    echo "   (then delete the auto-commit.sh line)"
    echo ""
    
    print_info "The first commit will happen in $CRON_INTERVAL minutes"
    print_warning "Remember to review and squash autocommits before merging!"
}

# Run main function
main "$@"
