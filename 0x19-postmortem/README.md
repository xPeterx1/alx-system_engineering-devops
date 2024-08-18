### Postmortem: Apache 500 Error Due to WordPress Configuration Issue

![Apache 500 Error Due to WordPress Configuration Issue](./image.png)

**Issue Summary:**

- **Duration:** The outage lasted from August 15, 2024, 02:00 UTC to August 15, 2024, 03:30 UTC (1 hour 30 minutes).
- **Impact:** The Apache web server returned a 500 Internal Server Error, affecting approximately 80% of users accessing the website during this period. Users experienced an inability to load the WordPress site, which led to a significant drop in traffic and potential revenue loss.
- **Root Cause:** A typo in the WordPress configuration file `wp-settings.php` where the class file extension `phpp` was mistakenly used instead of `php`.

**Timeline:**

- **02:00 UTC:** Issue detected by monitoring alerts indicating a spike in 500 errors.
- **02:05 UTC:** On-call engineer begins investigating the issue by checking Apache logs, which confirm multiple 500 errors but no clear root cause.
- **02:15 UTC:** Strace is used to attach to the running Apache process to trace system calls and signals, revealing an issue loading `class-wp-locale.phpp`.
- **02:25 UTC:** The engineer identifies the typo in `wp-settings.php` and suspects it as the root cause.
- **02:30 UTC:** Initial attempts to correct the typo manually and restart Apache are made, but the fix does not persist after the server is rebooted.
- **02:45 UTC:** The incident is escalated to the DevOps team to automate the fix using Puppet to ensure consistency.
- **03:10 UTC:** A Puppet script is created and applied to correct the typo across all relevant servers.
- **03:30 UTC:** The issue is resolved, and the site is fully operational. Monitoring confirms that 500 errors have ceased.

**Root Cause and Resolution:**

- **Root Cause:** The root cause of the outage was a typo in the WordPress configuration file `wp-settings.php`, where `phpp` was incorrectly used instead of `php` for the `class-wp-locale` file. This caused Apache to fail when loading the necessary PHP class, resulting in a 500 error.
  
- **Resolution:** The issue was resolved by creating a Puppet script to correct the typo across all affected servers. The Puppet script used a `sed` command to replace the incorrect `phpp` extension with `php`, ensuring that the fix would persist even after server reboots. The Apache service was restarted to apply the changes.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
  - Implement file integrity monitoring to detect unauthorized or accidental changes to critical configuration files.
  - Add automated tests to verify the integrity and correctness of key configuration files before deployment.
  - Enhance logging and error messages in Apache to provide more detailed information on file loading failures.

- **Tasks:**
  1. **Patch the WordPress `wp-settings.php` file** using Puppet to correct the typo.
  2. **Implement monitoring** on all configuration files for unauthorized changes.
  3. **Create automated tests** for configuration file validation during the CI/CD pipeline.
  4. **Update Apache error logging** settings to provide more detailed information in case of similar issues in the future.
