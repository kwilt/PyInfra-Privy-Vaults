# PyInfra-Privy-Vaults
This is an example of how you can use [privy](https://pypi.org/project/privy/) with [PyInfra](https://pyinfra.com/) in a way that mimics [Ansible Vaults](https://docs.ansible.com/ansible/latest/vault_guide/index.html) (sort of) 🙂.

Essentially, run `create_vault.py` (in the `vaults` directory) to make a "vault" file within that folder containing your encrypted data. Then, you can use a function like what I've made in `deploy.py` to decrypt the value to then pass into a Jinja template.
