#!/usr/bin/expect -f


set timeout 10
set username [lindex $argv 0]
set password [lindex $argv 1]
set realip   [lindex $argv 2]
set script   [lindex $argv 3]

spawn /usr/bin/ssh -l $username $realip "$script"

expect  {
    "(yes/no" {
        send "yes\n"
        expect "password:"
        send "$password\n"
    }
    "password:" {
        send "$password\n"
    }
}

expect eof
