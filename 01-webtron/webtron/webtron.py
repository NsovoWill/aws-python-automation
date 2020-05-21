import boto3
import click



session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron deploys websites to AWS"
    pass


@cli.command('list-buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "list all the files in the buckets"
    for objects in s3.Bucket(bucket).objects.all():
        print(objects)



if __name__ == "__main__":
    cli()