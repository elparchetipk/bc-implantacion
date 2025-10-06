#!/bin/bash
# ============================================
# auto-commit.sh - Autocommit Script with Conventional Commits
# ============================================
# What? Automated git commit script with conventional commit format
# For? Keep work-in-progress changes backed up automatically
# Impact? Reduces risk of data loss and maintains commit history
# ============================================

# Repository path - UPDATE THIS to your actual path
REPO_PATH="/home/epti/Documentos/epti-dev/bc-channel/bc-implantacion"

# Log file for debugging
LOG_FILE="$REPO_PATH/.autocommit.log"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Function to determine commit type based on changes
# What? Analyzes git diff to determine appropriate conventional commit type
# For? Automatically classify commits based on file changes
# Impact? More meaningful commit history without manual classification
determine_commit_type() {
    local changes="$1"
    
    # Check for different file types and determine commit type
    if echo "$changes" | grep -q "package.json\|requirements.txt\|composer.json\|Gemfile"; then
        echo "build"
    elif echo "$changes" | grep -q "\.md$\|README\|docs/"; then
        echo "docs"
    elif echo "$changes" | grep -q "\.svg$\|\.png$\|\.jpg$\|assets/"; then
        echo "style"
    elif echo "$changes" | grep -q "test\|spec\."; then
        echo "test"
    elif echo "$changes" | grep -q "docker-compose\|Dockerfile\|\.sh$"; then
        echo "chore"
    elif echo "$changes" | grep -q "\.gitignore\|\.editorconfig"; then
        echo "chore"
    elif echo "$changes" | grep -q "practicas/\|teoria/"; then
        echo "feat"
    else
        echo "chore"
    fi
}

# Function to generate commit scope
# What? Determines the scope based on changed directories
# For? Add context to commits about which part of project was modified
# Impact? Better commit organization and searchability
determine_commit_scope() {
    local changes="$1"
    
    if echo "$changes" | grep -q "semana-01/"; then
        echo "week-01"
    elif echo "$changes" | grep -q "semana-02/"; then
        echo "week-02"
    elif echo "$changes" | grep -q "semana-03/"; then
        echo "week-03"
    elif echo "$changes" | grep -q "semana-04/"; then
        echo "week-04"
    elif echo "$changes" | grep -q "semana-05/"; then
        echo "week-05"
    elif echo "$changes" | grep -q "semana-06/"; then
        echo "week-06"
    elif echo "$changes" | grep -q "semana-07/"; then
        echo "week-07"
    elif echo "$changes" | grep -q "semana-08/"; then
        echo "week-08"
    elif echo "$changes" | grep -q "semana-09/"; then
        echo "week-09"
    elif echo "$changes" | grep -q "assets/"; then
        echo "assets"
    elif echo "$changes" | grep -q "\.github/"; then
        echo "config"
    elif echo "$changes" | grep -q "_docs/"; then
        echo "docs"
    else
        echo "general"
    fi
}

# Function to generate commit message
# What? Creates a descriptive commit message following conventional commits
# For? Provide meaningful context about what changed, why, and impact
# Impact? Better project history and easier to understand changes later
generate_commit_message() {
    local commit_type="$1"
    local commit_scope="$2"
    local file_count="$3"
    local timestamp=$(date '+%Y-%m-%d %H:%M')
    
    # Base message with type and scope
    local message="${commit_type}(${commit_scope}): auto-save progress"
    
    # Add body with details (what, for, impact)
    local body=""
    body+="What: Automated commit of ${file_count} changed file(s)\n"
    body+="For: Preserve work-in-progress and maintain backup\n"
    body+="Impact: Incremental progress saved at ${timestamp}\n"
    body+="\n"
    body+="Note: Automated commit by cron job"
    
    echo -e "${message}\n\n${body}"
}

# Main execution
# What? Main workflow: check changes, create commit, push to remote
# For? Automate the entire process of backing up work
# Impact? Hands-free backup every 5 minutes
main() {
    log_message "=== Starting autocommit process ==="
    
    # Change to repository directory
    cd "$REPO_PATH" || {
        log_message "ERROR: Cannot access repository at $REPO_PATH"
        exit 1
    }
    
    # Check if it's a git repository
    if [ ! -d .git ]; then
        log_message "ERROR: Not a git repository"
        exit 1
    fi
    
    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        log_message "INFO: No changes to commit"
        exit 0
    fi
    
    # Get list of changed files
    changed_files=$(git status --porcelain | awk '{print $2}')
    file_count=$(echo "$changed_files" | wc -l)
    
    log_message "INFO: Found $file_count changed file(s)"
    
    # Determine commit type and scope
    commit_type=$(determine_commit_type "$changed_files")
    commit_scope=$(determine_commit_scope "$changed_files")
    
    log_message "INFO: Commit type: $commit_type, scope: $commit_scope"
    
    # Stage all changes
    git add -A
    
    # Generate and apply commit message
    commit_message=$(generate_commit_message "$commit_type" "$commit_scope" "$file_count")
    
    # Commit changes
    if git commit -m "$commit_message"; then
        log_message "SUCCESS: Committed changes"
        
        # Try to push (optional, will fail silently if no remote or network issues)
        if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
            log_message "SUCCESS: Pushed to remote"
        else
            log_message "WARNING: Could not push to remote (may not be critical)"
        fi
    else
        log_message "ERROR: Commit failed"
        exit 1
    fi
    
    log_message "=== Autocommit process completed ==="
}

# Execute main function
main
