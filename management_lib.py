import boto3
import json
import pprint

# for launching new instances see: http://boto3.readthedocs.io/en/latest/guide/migrationec2.html#launching-new-instances
# ec2 managment
ec2 = boto3.resource('ec2')
sqs = boto3.client('sqs')
client = boto3.client('ec2')

def list_running():
   instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
   for instance in instances:
       print(instance.id, instance.instance_type)

def list_ips():
   instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
   for instance in instances:
       print(instance.id, instance.public_ip_address)

def list_health():
    for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
       print(status)

def list_by_label():
    instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
       print(instance.id, instance.public_ip_address, instance.tags)

# ids = ['list, 'of', 'machine-ids']
# or
# ids = ['one-machine-id'] just remember, it must be in list form, which means square brakcets and single quotes.
def stop_by_id(ids):
   ec2.instances.filter(InstanceIds=ids).stop()

def env_2_json():
   response = client.describe_instances()
   pprint.pprint(response)
