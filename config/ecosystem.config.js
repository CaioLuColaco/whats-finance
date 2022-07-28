module.exports = {
    apps: [
        {
            name: 'whats-finance',
            script: 'index.py',
            watch: ['index'],
            cwd: './',
            log_date_format: 'DD-MM-YYYY HH:mm:ss',
            out_file: `\\\\${process.env.LOG_PATH}\\Logs\\whats-finance\\whats-finance_output.log`,
            error_file: `\\\\${process.env.LOG_PATH}\\Logs\\whats-finance\\whats-finance_error.log`
        }
    ]
}
