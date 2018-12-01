import boto3

access_key_id="AKIAJLOE6GCPBQJW7BOA"
secret_access_key="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"
sg_file=open('security-groups.txt','w+')
#regions=['ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-1','us-west-2']
regions=['us-west-1','us-west-2']
print "hello program has initiated.........."
def create_security_groups():
	for region in regions:
		ec2=boto3.resource('ec2',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name=region)
		print "ec2 object init--"
		try:
			sec_group=ec2.create_security_group(GroupName='web_access', Description='for access to web port 80')
			sec_group.authorize_ingress(CidrIp='0.0.0.0/0',IpProtocol='tcp',FromPort=80,ToPort=80)
			print ("security group created....................")
			print (sec_group.id)
			sg_file.write(region+' '+sec_group.id)
			sg_file.write("\n")
		except:
			print ("excpetion in.."+' '+region)
			sg_file.write("exception_occurred in"+' '+region)
			sg_file.write("\n")


def main():
	create_security_groups()

main();