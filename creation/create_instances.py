import boto3
import json
access_key_id="AKIAJLOE6GCPBQJW7BOA"
secret_access_key="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"
instance_file=open('instances-list.txt','w+')
print "hello program has initiated.........."
def create_instances_call():
	with open('aws_details.json', 'r') as f:
		aws_client = json.load(f)
		for aws in aws_client:
			print("hi"+' '+aws['Region']+' '+aws['Ami']+' '+aws['Security_Group'])
			#creating ec2 object 
			ec2=boto3.resource('ec2',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name=aws['Region'])
			print "ec2 object init--"
			try:
				#Creating instance with ami,security groups from JSON
				instances = ec2.create_instances(ImageId=aws['Ami'],InstanceType=aws['Instance_Type'],MaxCount=1, MinCount=1,SecurityGroups=[aws['Security_Group']])
				print ("instance created")
				for iterator in instances:
					iterator.wait_until_running()
					instance=ec2.Instance(iterator.id)
					print (iterator.id,instance.public_ip_address)
					instance_file.write(iterator.id)
					instance_file.write(" ")
					instance_file.write(instance.public_ip_address)
					print ("\n")
					instance_file.write("\n")
					#print("instance-id: "+' '+instances[0].id,+' '+"instance-ip :"+' '+instance.public_ip_address)
					#instance_file.write(region,' '+instances[0].id+' '+instance.public_ip_address)
					#instance_file.write("\n")
			except:
				print ("excpetion in.."+' '+aws['Region'],aws['Ami'])
				instance_file.write("exception_occurred in"+' '+aws['Region']+' ')
				instance_file.write("\n")
		



def main():
	create_instances_call()

main();