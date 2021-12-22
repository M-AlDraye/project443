from kubernetes import client, config

config.load_kube_config()


def delete_pod(name, namespace):
    core_v1 = client.CoreV1Api()
    delete_options = client.V1DeleteOptions()
    api_response = core_v1.delete_namespaced_pod(
        name=name,
        namespace=namespace,
        body=delete_options)
    print(api_response)


if __name__ == '__main__':
    delete_pod(name='jj4', namespace='default')