MY_TEAM_ID = 5

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.
    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    "TEAMS": {
        "Team #{}".format(i): "10.80.{}.2".format(i)
        for i in range(2,11)
    },
    "FLAG_FORMAT": r"[A-Z]{31}=",
    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.
    "SYSTEM_PROTOCOL": "ructf_http",
    # "SYSTEM_HOST": "127.0.0.1",
    # "SYSTEM_PORT": 31337,
    # 'SYSTEM_PROTOCOL': 'ructf_http',
    'SYSTEM_URL': 'http://10.10.10.10/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',
    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',
    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    "SUBMIT_FLAG_LIMIT": 50,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    "SERVER_PASSWORD": "WobyhCoolFarm",
    # Use authorization for API requests
    "ENABLE_API_AUTH": True,
    "API_TOKEN": "UZz5t82ty84DU6ZgXASA",
}
