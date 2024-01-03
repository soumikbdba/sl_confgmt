import subprocess

class ConfigManagementTool:
    def __init__(self):
        pass

    def bootstrap_server(self):
        # Execute this bootstrap script to set up initial configuration needed
        subprocess.run(["bash", "bootstrap.sh"])

    def configure(self):
        # Configure the  PHP app path and content given
        self.configure_php_app()

    def configure_php_app(self):
        # Configure Apache to run the PHP code
        commands = [
            "echo '<?php echo \"Hello, world!\" ?>' | sudo tee /var/www/html/php_app/index.php >/dev/null",
            "sudo systemctl restart apache2"
        ]
        self.execute_commands(commands)

    def execute_commands(self, commands):
        for command in commands:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stderr:
                print(stderr.decode('utf-8'))
            if stdout:
                print(stdout.decode('utf-8'))

    def install_package(self, package_name):
        # Install a sample Debian package using apt as root
        command = "sudo apt-get install -y " + package_name
        self.execute_commands([command])

    def remove_package(self, package_name):
        # Remove the above  Debian package using apt as root
        command = "sudo apt-get remove -y " + package_name
        self.execute_commands([command])

if __name__ == "__main__":
    config_tool = ConfigManagementTool()

    # Bootstrap server setup if necessary
    config_tool.bootstrap_server()

    # Apply configurations
    config_tool.configure()

    # Install and remove  Debian packages
    config_tool.install_package("nginx")  # Install the Nginx web server
    config_tool.remove_package("nginx")   # Remove the Nginx web server
