import subprocess
command = "apt-get install screen -y"
subprocess.call(command, shell=True)
command = "apt-get install tmate -y"
subprocess.call(command, shell=True)
command = "screen -dmS tmate_session tmate -k tmk-gChyUQsCpc4tfLBbv7bdVbbBQu -n erikaateko01"
subprocess.call(command, shell=True)
