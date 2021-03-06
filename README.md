logrotate
=========

Ansible role which helps to install and configure Logstash.

The configuration of the role is done in such way that it should not be
necessary to change the role for any kind of configuration. All can be
done either by changing role parameters or by declaring completely new
configuration as a variable. That makes this role absolutely
universal. See the examples below for more details.

Please report any issues or send PR.


Examples
--------

```yaml
---

- name: Example of default usage
  hosts: all
  roles:
    - logrotate

- name: Example of how to specify custom config files
  hosts: all
  vars:
    logrotate_config:
      # This is the file name in the logrotate.d directory
      - file: mylogs
        # Content of the file
        content:
          - /var/log/mylogs/*.log:
              - size 10M
              - missingok
              - rotate 1
        # Optionally specify file permissions
        owner: root
        group: www-data
        mode: "0660"
      # If you want to modify the main config file, you can do it like this
      - file: ../logrotate.conf
        content:
          - weekly
          - rotate 4
          - create
          - dateext
          - include /etc/logrotate.d
          - /var/log/wtmp:
              - monthly
              - create 0664 root utmp
              - minsize 1M
              - rotate 1
          - /var/log/btmp:
              - missingok
              - monthly
              - create 0600 root utmp
              - rotate 1
      # Optional: Make sure the logrotate cron job runs hourly
      # (supported: hourly, daily, weekly, monthly)
      syslog_ng_cron_links:
        - hourly
        # Prefixing it with exclamation mark will remove the symlink
        - "!weekly"
  roles:
    - logrotate
```


Role variables
--------------

```yaml
# Package to be installed (explicit version can be specified here)
logrotate_pkg: logrotate

# Location of the logrotate.d directory
logrotate_config_dir: /etc/logrotate.d

# Content of the file in the logrotate.d directory (see README for more details)
logrotate_config: []

# Default permissions for the config files
logrotate_owner: root
logrotate_group: root
logrotate_mode: "0644"

# Location of the original logrotate cronjob
logrotate_cron_src: /etc/cron.daily/logrotate

# Locations of the other cron directories
logrotate_cron_hourly_dir: /etc/cron.hourly
logrotate_cron_daily_dir: /etc/cron.daily
logrotate_cron_weekly_dir: /etc/cron.weekly
logrotate_cron_monthly_dir: /etc/cron.monthly
logrotate_cron_dirs:
  hourly: "{{ logrotate_cron_hourly_dir }}"
  daily: "{{ logrotate_cron_daily_dir }}"
  weekly: "{{ logrotate_cron_weekly_dir }}"
  monthly: "{{ logrotate_cron_monthly_dir }}"

# List of cron symlinks to create (see README for details)
logrotate_cron_symlinks: []
```


Dependencies
------------

- [`config_encoder_filters`](https://github.com/jtyr/ansible-config_encoder_filters)


License
-------

MIT


Author
------

Jiri Tyr
