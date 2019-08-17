import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from proxmoxer import ProxmoxAPI

class Proxmox:

    def __init__(self):
        self.proxmoxHost = '192.168.20.140';
        self.proxmoxUser = 'root'
        self.proxmoxKeyFile = '/Users/charl/.ssh/id_rsa_proxmox'
        self.proxmoxAPI = ProxmoxAPI(host = proxmoxHost, user = proxmoxUser, backend='ssh_paramiko', private_key_file = proxmoxKeyFile)

    def create(
        lvm_name,
        hostname,
        type = 'lxc', 
        vmid = '211', 
        ostemplate='local:vztmpl/debian-9.0-standard_9.3-1_amd64.tar.gz', 
        cluster_node = 'pve',
        storage = 'local-lvm',
        disk_size = '2G',
        memory = 512,
        swap = 512,
        cores = 1,
        password = 'datb@ss',
        net='name=eth0,bridge=vmbr0,ip=192.168.20.143/20,gw=192.168.20.254'
        ):

        lvm_name = 'vm-{0}-disk-{1}'.format(vmid, vm_disk_counter)
        hostname = 'host %d' % vmid

        node = proxmox.nodes(cluster_node)
        proxmox.nodes('pve').storage('local-lvm').content().create(vmid = vmid, format = 'raw', filename = lvm_name, size = disk_size)
        node.format_lvm(lvm_name = lvm_name, filesystem = 'ext4')
        result = node.lxc.create(vmid=vmid,
            ostemplate=ostemplate,
            hostname=hostname,
            storage=storage,
            memory=memory,
            swap=swap,
            cores=cores,
            password=password,
            rootfs='local-lvm:%s,size=%s' % (lvm_name, disk_size),
            net0=net)
        proxmox.nodes(cluster_node).lxc('%d' % vmid).status().start().create()

        return result
