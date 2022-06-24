module main

import os
import cli
import function

fn main() {
    mut app := cli.Command{
        name: 'powermode'
        description: 'CLI tool for powerprofiles ctl'
        version: '2.0.0'
        execute: fn (cmd cli.Command) ? {
            function.get_mode()
            return
        }
        commands: [
            cli.Command{
                name: 'power'
                description: 'Sets Power mode'
                execute: fn (cmd cli.Command) ? {
                    function.performance()
                    exit(0)
                }
            }
            cli.Command{
                name: 'balanced'
                description: 'Sets balanced mode'
                execute: fn (cmd cli.Command) ? {
                    function.balanced()
                    exit(0)
                }
            }
            cli.Command{
                name: 'saving'
                description: 'Sets Power-saving mode'
                execute: fn (cmd cli.Command) ? {
                    function.power_saver()
                    exit(0)
                }
            }
        ]
    }
    app.setup()
    app.parse(os.args)
}

