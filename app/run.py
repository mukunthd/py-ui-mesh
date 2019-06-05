from flask import Flask, render_template, request, send_from_directory
import boto3

profile_name = '<profile_Name>'
boto3.setup_default_session(profile_name=profile_name)


app = Flask(__name__)


@app.route('/')
def template():
    return render_template('index.html')


@app.route('/app', methods=['POST'])
def aws():
    service_list = []
    app_id_get = request.form['app_id_get']
    region = request.form['region']
    print(region)
    try:
        service_list.append(request.form['service_type'])
    except Exception as e:
        print('Error')
    try:
        service_list.append(request.form['service_type1'])
    except Exception as e:
        print('Error')
    try:
        service_list.append(request.form['service_type2'])
    except Exception as e:
        print('Error')
    try:
        service_list.append(request.form['service_type3'])
    except Exception as e:
        print('Error')
    try:
        service_list.append(request.form['service_type4'])
    except Exception as e:
        print('Error')
    try:
        service_list.append(request.form['service_type5'])
    except Exception as e:
        print('Error')
    service_list.append('elasticloadbalancing')
    boto3.setup_default_session(profile_name=profile_name)
    client = boto3.client('resourcegroupstaggingapi', region_name=region)

    paginator = client.get_paginator('get_resources')
    response_iterator = paginator.paginate(
        TagFilters=[
            {
                'Key': 'app_id',
                'Values': [
                    app_id_get
                ]
            },
        ],
        # TagsPerPage=100,
        ResourceTypeFilters=service_list,
        PaginationConfig={
            'MaxItems': 100,
            'PageSize': 20,
            'StartingToken': ''
        }
    )

    lis = [
    ]

    print(type(response_iterator))
    for pages in response_iterator:
        # print(type(pages))
        # for key in pages:
        a = pages['ResourceTagMappingList']
        index = 0
        while index < len(a):
            # print(a[index]['ResourceARN'])
            lis.append([(a[index]['ResourceARN'])])
            index = index + 1
            # print(lis)
        if not lis:
            print('Nothing')
        else:
            print('hello')

    print('list of items', lis)

    a = (len(lis))
    items = [

    ]

    def item_list():
        index = 0
        while index < len(lis):
            items.append(lis[index])
            index = index + 1
    try:
        item_list()
    except Exception as e:
        print('error')

    db_details = {

    }
    ec2_details = {

    }
    ec2_details_for = {

    }

    db_resources_details = [

    ]
    my_db_storage = [

    ]
    my_dbs_hosts = [

    ]
    my_db_instance_status = [

    ]

    my_db_instance_types = [

    ]
    my_multiaza = [

    ]
    # print(type(items()
    loadbalancer_details_lb = [

    ]
    target_details = [

    ]
    def resources():
        index = 0
        while index < len(items):
            b = items[index]
            # print(type(b))
            c = (', '.join(b))
            d = c.split(":")
            # print(d[2])
            # print(d)
            # print(f)
            # print('assdsdfsfsfdsfsfdsfdfdf', d)
            index = index + 1
            # service_list.append(f)
            if d[2] == 'rds' and d[5] == 'db':
                print(d)
                h = db_details[index] = d[6]
                print(h)
                db_resources_details.append(h)
                # print(resource_details)
            elif d[2] == 'ec2':
                e = (', '.join(d))
                f = e.split("/")
                # print(f[1])
                if f[1].startswith('i-') == True:
                    ec2_details[index] = f[1]
                    ec2_details_for[0] = f[1]
            elif d[2] == 'elasticloadbalancing':
                abc = d[5]
                yyy = abc.split("/")
                xyx = yyy[2]
                #print('THISSSSS YYYYYYY', yyy)
                #print('THISSSSS YYxxxYYYYY', xyx)
                if yyy[0] == 'loadbalancer':
                    loadbalancer_details_lb.append(xyx)
                else:
                    target_details.append(xyx)
                #loadbalancer_details.append(d[5])
    try:
        resources()
    except Exception as e:
        print('Eror')
    try:
        for i in db_resources_details:
            db_instance = i
            source = boto3.client('rds', region_name=region)
            instances = source.describe_db_instances(DBInstanceIdentifier=db_instance)
            # print(instances)
            rds_host = instances.get('DBInstances')[0].get('Endpoint').get('Address')
            instance_type = instances.get('DBInstances')[0].get('DBInstanceClass')
            multiaz = instances.get('DBInstances')[0]['MultiAZ']
            # print(multiaz)
            instance_status = instances.get('DBInstances')[0].get('DBInstanceStatus')
            storage = instances.get('DBInstances')[0]['AllocatedStorage']

            my_dbs_hosts.append(rds_host)
            my_db_instance_types.append(instance_type)
            my_multiaza.append(multiaz)
            my_db_instance_status.append(instance_status)
            my_db_storage.append(storage)
        #print(my_dbs_hosts)
        #print(my_db_instance_types)
        #print(my_multiaza)
        #print(my_db_instance_status)
    except Exception as e:
        print('NO DB')

    print('This is Load Balancer', loadbalancer_details_lb)
    print('This is Target Group', target_details)
    a = ec2_details.values()

    cluster_names = [

    ]

    repo_names = [

    ]
    ec2_instance_details = {

    }
    image_id = [

    ]
    instance_type = [

    ]
    IPAddress = [

    ]
    running_state = [

    ]

    def describe_instances():
        for i in a:
            client = boto3.client('ec2', region_name=region)
            response = client.describe_instances(
                InstanceIds=[
                    i,
                ]
            )
            # index = index + 1
            # print(type(response['Reservations'][0]['Instances'][0]))
            # print(response)
            for key in response:
                instance_b = response['Reservations']
                print('bbbbbbb', instance_b)
                print(len(instance_b))
                instance_c = instance_b[0]
                #print('asdadsadadas', type(c))
                d = instance_c['Instances']
                print('ssssss', d)
                e = d[0]
                f = e['Tags']
                running = e['State']
                state = running['Name']
            
                if profile_name == 'apps':
                    index = 0
                    while index < len(f):
                        g = f[index]
                        if "ecs_cluster_name" in g.values():
                            # print(g)
                            cluster_names.append(g['Value'])
                        index = index + 1
                else:
                    index = 0
                    while index < len(f):
                        g = f[index]
                        if "Name" in g.values():
                            # print(g)
                            cluster_names.append(g['Value'])
                        index = index + 1

                        # print(g)
                index = 0
                while index < len(f):
                    g = f[index]
                    if "tf_repo" in g.values():
                        # print(g)
                        repo_names.append(g['Value'])
                    index = index + 1
                imageid = e['ImageId']
                LaunchTime = e['LaunchTime']
                SubnetId = e['SubnetId']
                InstanceType = e['InstanceType']
                PrivateIpAddress = e['PrivateIpAddress']
            image_id.append(imageid)
            instance_type.append(InstanceType)
            IPAddress.append(PrivateIpAddress)
            running_state.append(state)
            # print(f[16])
            # print(g)

            # print(imageid, LaunchTime, SubnetId, InstanceType, PrivateIpAddress)

    try:
        describe_instances()
    except Exception as e:
        print('Error')
    elasticlis = [

    ]

    elasticlis_updated = [

    ]
    elastic_value_empty = 'No Elastic Cache'
    if not elasticlis:
        elasticlis_updated.append(elastic_value_empty)
    else:
        elasticlis_updated = elasticlis
    cluster_names_values1 = (set(cluster_names))
    print('BEFOR ELAS', cluster_names_values1)
    def elastic():
        boto3.setup_default_session(profile_name=profile_name)
        paginator = client.get_paginator('get_resources', region_name=region)
        response_iterator = paginator.paginate(
            TagFilters=[
                {
                    'Key': 'name',
                    'Values': cluster_names_values1
                    # 'Values': ['cart-latest']
                },
            ],
            # TagsPerPage=100,
            ResourceTypeFilters=['elasticache'],
            PaginationConfig={
                'MaxItems': 100,
                'PageSize': 20,
                'StartingToken': ''
            }
        )

        print('eeelasticccccc')
        print(response_iterator)
        for pages in response_iterator:
            # print(type(pages))
            # for key in pages:
            a = pages['ResourceTagMappingList']
            index = 0
            while index < len(a):
                # print(a[index]['ResourceARN'])
                # elasticlis.append([(a[index]['ResourceARN'])])
                b = a[index]['ResourceARN']
                print('elasssticcccccmukkkk', b)
                # d = (', '.join(b))
                e = b.split(":")
                elasticlis.append(e[6])
                index = index + 1
                # print(lis)
            if not elasticlis:
                print('Nothing')
            else:
                print('hello')

    try:
        elastic()
    except Exception as e:
        print('error')

   

    mydict = {

    }
    ecs_service_list = [

    ]
    cluster_names_values1 = (set(cluster_names))
    print("HEEeEEEEEEE", cluster_names_values1)

    def main_run():
        for i in cluster_names_values1:
            def cluster():
                # global response
                client = boto3.client('ecs', region_name=region)
                response = client.describe_clusters(
                    clusters=[i],
                )
                return response

            exe = cluster()
            a = exe['clusters']
            # mydict[i] = a[0]['clusterName']
            mydict[a[0]['clusterName']] = a[0]['status']

    try:
        main_run()
    except Exception as e:
        print('Error')

    total_cost = {

    }

    def cost():
        client = boto3.client('ce')

        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': '2018-10-19',
                'End': '2018-11-19'
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            Filter={
                'Tags': {
                    'Key': 'app_id',
                    'Values': [
                        app_id_get,
                    ],
                }
            }
            # GroupBy=[
            #          {'Type': 'DIMENSION',
            #           'Key': 'SERVICE'
            #          }
            # ]
        )
        # print(response)
        # print(type(response))
        print(response)
        a = response['ResultsByTime']
        print(len(a))
        index = 0
        while index < len(a):
            b = a[index]['Total']['UnblendedCost']['Amount']
            # c = b + b
            # total_cost.append(b)
            total_cost['Total Cost in USD'] = b
            index = index + 1

    # cost()
    # print(mydict)

    print('No Of DB', len(db_details), db_details.values())
    print('No Of EC2', len(ec2_details), ec2_details.values())
    number_of_resources = (len(lis))
    # number_of_instances = len(db_details)
    number_of_db_instances = len(ec2_details)
    db_instance__values = ec2_details.values()
    # instance_details = ec2_details.values()
    instance_details = list(ec2_details.values())
    db_details = db_resources_details

    cluster_names_values = (set(cluster_names))
    repo_names_values = (set(repo_names))
    print(type(repo_names_values))
    ecs_cluster_status = mydict
    print(ecs_cluster_status)
    elastic_list = elasticlis_updated

    # id=seperate_id, service_type=service_list, region=region, lang=True)
    return render_template('Report.html', lisa=number_of_resources, ec2_details=instance_details,
                           service_type=service_list, region=region, lang=True,
                           cluster_name_values=cluster_names_values, repo_names_values=repo_names_values, mydict=mydict,
                           ecs_service_list=ecs_service_list, instance_type=instance_type, IPAddress=IPAddress,
                           image_id=image_id, total_cost=total_cost, app_id_get=app_id_get, db_details=db_details,
                           running1=running_state, elasticlis=elastic_list, my_db_instance_types=my_db_instance_types, my_dbs_hosts=my_dbs_hosts, my_db_instance_status=my_db_instance_status, my_multiaza=my_multiaza )


@app.route('/cluster', methods=['POST', 'GET'])

def cluster_details():
   
    cluster_names = [request.form['cluster_name_from']]
    mydict = {

    }

    #####Application_Service is the list of services
    application_service = [

    ]
    service_count = [

    ]
    application_list = [

    ]

    total = [

    ]
    service_a = [

    ]
    status_b = [

    ]
    desired_c = [

    ]
    running_d = [

    ]

    def cluster():
        # global response
        client = boto3.client('ecs', region_name='us-west-2')
        response = client.describe_clusters(
            clusters=cluster_names,
        )
        return response

    print(cluster())

    exe = cluster()
    a = exe['clusters']
    # mydict[i] = a[0]['clusterName']
    mydict[a[0]['clusterName']] = a[0]['status']

    # cluster_name = mydict['Cluster Name']
    # cluster_name = i

    cluster_names = cluster_names[0]
    print(cluster_names)

    def ecs_services():
        # global response
        client = boto3.client('ecs', region_name='us-west-2')
        response = client.list_services(
            cluster=cluster_names
        )
        return response

    try:
        ecs_services()
    except Exception as e:
        print("Error")
    # print(type(response))
    print('eccssssss', ecs_services())

    index = 0
    for key in ecs_services():
        a = ecs_services()['serviceArns']
        while index < len(a):
            b = [a[index]]
            # print(type(b))
            c = (', '.join(b))
            d = c.split(":")
            e = (', '.join(d))
            f = e.split("/")
            g = (f[1])
            application_service.append(g)
            # print(d)
            index = index + 1

            # service_list.append(f)
    #print(application_service)  # Service List
    try:
        for i in application_service:
            def describe_services():
                # global response
                client = boto3.client('ecs', region_name='us-west-2')
                response = client.describe_services(
                    cluster=cluster_names,
                    services=[i]
                    
                )
                return response

            # print(describe_services())

            output = describe_services()
            value = 0
            for key in output:
                services = output['services']
                # print(len(services))
                while value < len(services):
                    get_list = (services[value])
                    # print('ServiceName =', get_list['serviceName'], 'STATUS', get_list['status'], 'DesiredCount', get_list['desiredCount'], 'Running Count', get_list['runningCount'])#Service Status
                    a = get_list['serviceName']
                    b = get_list['status']
                    c = get_list['desiredCount']
                    d = get_list['runningCount']
                    # service_count_dict[get_list['serviceName']], ['STATUS'] = get_list['status'],['DesiredCount'] = get_list['desiredCount'], ['Running Count',get_list['runningCount'])
                    application_list.append({a, b, d})
                    value = value + 1
            service_a.append(a)
            status_b.append(b)
            desired_c.append(c)
            running_d.append(d)
    except Exception as e:
        print('Error')

    def list_container_instances():
        client = boto3.client('ecs')
        response = client.list_container_instances(
            cluster=cluster_names,
            status='ACTIVE'
        )
        return response

    print(total)
    print(len(total))

    return render_template('cluster.html', service_a=service_a, status_b=status_b, desired_c=desired_c,
                           running_d=running_d, cluster_name=cluster_names)


if __name__ == '__main__':
    app.run(debug=True)
