# VM-Spin

As a developer, you may want to open up a VM for a linux distro! Docker is often the best solution as it is light weight! However, Docker Desktop can be slow or hard to use sometimes...we make it easy!

Using our Python CLI, you can spin up a Linux VM in a few seconds! It uses Docker tech under the hood but hides all the useless overhead so that you can start creating VMs quickly!

## Usage
To use this, run `git clone`.

Run: `pip install -r requirements.txt`

To create a linux vm, run:
```
python3 vm.py create <name of distro> <name of vm>
```

To use the linux vm, run:
```
python3 vm.py run <name of vm>
```
This opens up the terminal for the specified distro!

To stop a certain VM, run:
```
python3 main.py vm <name of vm>
```
