# Send Me My Internet Usage Statistics

Simple utility to send internet usage statistics using vnstat and vnstati linux utilities.

### Daily Stats

![Daily Summary](img/daily_summary.png)t

### Monthly Stats

![Daily Summary](img/monthly_summary.png)

# Install

    $ sudo apt install vnstat && sudo apt install vnstati

With pip3 installed

     $ pip3 install email-to

# Run script

    $ python daily.py

    or

    $ python monthly.py

# Schedule with Crontab

Add the following to crontab -e

    # at the top of crontab -e
    SHELL=<path-to-shell>
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # at the bottom of crontab -e

    # send daily internet usage stats at 11:59 PM every day
    59 23 * * * source ~/.<shell-rc-file> && python <path-to-daily.py>

    # send monthly internet usage stats at the last day of the month
    59 23 28-31 * * source ~/.<shell-rc-file> && python <path-to-monthly.py>
