import json
import boto3

# Authentication to AWS access key and id,
access_key_id="AKIAJT3QKUL6EMXBSXGA"
secret_access_key="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"

regions=['ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-1','us-west-2']
instances_list=[]
def delete_instances():
	for region in regions:
		ec2=boto3.resource('ec2',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name=region)
		print ("Looking for instances in: "+' '+region)
		for i in ec2.instances.all():
			instances_list.append(i)
		for instance in instances_list:
			print ("found instance :"+' '+instance.id)
			print ("\n")
			print ("Terminating instance :"+' '+instance.id)
			instance.terminate()


def main():
	delete_instances()
main()