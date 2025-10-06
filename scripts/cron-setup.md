# ============================================

# Cron Job Setup for Fedora 42

# ============================================

# What? Configuration file for automated git commits every 5 minutes

# For? Automatic backup of work-in-progress changes

# Impact? Reduces risk of data loss during bootcamp development

# ============================================

# Installation Instructions:

# 1. Copy the auto-commit.sh script to your preferred location

# 2. Update REPO_PATH in auto-commit.sh with your actual repository path

# 3. Make the script executable: chmod +x /path/to/auto-commit.sh

# 4. Install this cron job: crontab -e

# 5. Add the line below (uncommented)

# 6. Save and exit

# ============================================

# Cron Job Entry (runs every 5 minutes)

# ============================================

# Format: minute hour day month day-of-week command

# _/5 _ \* \* \* /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/scripts/auto-commit.sh >> /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/.autocommit.log 2>&1

# ============================================

# What each field means:

# ============================================

# \*/5 - Every 5 minutes

# \* - Every hour

# \* - Every day of month

# \* - Every month

# \* - Every day of week

# command - Path to the script with output redirection

# ============================================

# Alternative Schedules:

# ============================================

# Every 10 minutes:

# _/10 _ \* \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# Every 15 minutes:

# _/15 _ \* \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# Every 30 minutes:

# _/30 _ \* \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# Every hour:

# 0 \* \* \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# Only during work hours (9 AM to 6 PM, every 5 minutes):

# _/5 9-18 _ \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# Only on weekdays (Monday to Friday, every 5 minutes):

# _/5 _ \* \* 1-5 /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# ============================================

# Setup Commands for Fedora 42:

# ============================================

# 1. Ensure git is installed:

# sudo dnf install git -y

# 2. Configure git (if not already done):

# git config --global user.name "Your Name"

# git config --global user.email "your.email@example.com"

# 3. Test the script manually first:

# /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/scripts/auto-commit.sh

# 4. Edit crontab:

# crontab -e

# 5. Add the cron job line (see above)

# 6. Verify cron job is installed:

# crontab -l

# 7. Check cron service status:

# systemctl status crond

# 8. Enable cron service if not running:

# sudo systemctl enable --now crond

# ============================================

# Monitoring and Troubleshooting:

# ============================================

# View autocommit log:

# tail -f /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/.autocommit.log

# View last 50 lines of log:

# tail -n 50 /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/.autocommit.log

# Check if cron is running:

# ps aux | grep crond

# View system cron logs:

# journalctl -u crond -f

# Test cron job manually:

# /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/scripts/auto-commit.sh

# ============================================

# Disabling the Cron Job:

# ============================================

# 1. Edit crontab:

# crontab -e

# 2. Comment out the line by adding # at the beginning:

# # _/5 _ \* \* \* /path/to/auto-commit.sh >> /path/to/.autocommit.log 2>&1

# 3. Or remove the cron job entirely:

# crontab -r # WARNING: This removes ALL cron jobs for the user

# ============================================

# Security Considerations:

# ============================================

# - The script never commits sensitive files (.env, keys, etc) due to .gitignore

# - Logs are stored locally and should be reviewed periodically

# - Consider using SSH keys for git push to avoid credential prompts

# - Review commits before pushing to shared branches

# ============================================

# Best Practices:

# ============================================

# - Review autocommits periodically and squash them before merging

# - Use feature branches for actual development

# - Keep the main branch clean with meaningful commits

# - Consider using 'git rebase -i' to clean up autocommit history

# - Don't rely solely on autocommits - still make manual meaningful commits
