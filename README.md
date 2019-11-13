# Classification banners app for Openshift

This app is intended to be hosted on an OpenShift cluster to have a single location where the various system components can call out to, receive a `banner.js` file, and layer the appropriate colored banner over the console.

## Deployment Steps

To deploy this application from the OpenShift web console, you should select ``python:2.7``, ``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

Ensure you have the appropriate python image stream in your cluster (this always takes extra steps in a disconnected environment). 
From a cluster-admin account:
```
oc get is -n openshift | grep python
```

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this application, you can run:

```
oc new-app https://github.com/mbach04/openshift-classification-banners.git
```

In this case, because no language type was specified, OpenShift will determine the language by inspecting the code repository. Because the code repository contains a ``requirements.txt``, it will subsequently be interpreted as including a Python application. When such automatic detection is used, ``python:latest`` will be used. Ensure you have a `latest` tagged Python reference in your Python image stream.

If needing to select a specific Python version when using `oc new-app`, you should instead use the form:

```
oc new-app python:2.7~https://github.com/mbach04/openshift-classification-banners.git
```
## Disconnected environments
It's most likely you will need to build this application on the low side, export the docker image to a tar file, then re-import the image to your high side docker registry.

In that case, once you have the image located in a registry, you can run the `oc new-app` command.
In this example, the image has been pushed into the clusters default registry under the `openshift` namespace as `ocp-class-banners` and tagged with `latest`. Fill in your registry and classification as needed:
```
oc new-app {{ registry }}/openshift/ocp-class-banners:latest --insecure-registry --env CLASSIFICATION='{{ classification }}'
```
Note: For multiple word classifications (ie TOP SECRET) you will need to quote the value `CLASSIFICATION="TOP SECRET"`

Expose the route:
```oc create route edge --service=ocp-class-banners --hostname=banners.apps.example.com"```


## Banner Options
The color and banner text are selected by setting the environment variable `CLASSIFICATION` on the pod. 
Options are:
- "TOP SECRET"
- SECRET
- CONFIDENTIAL
- UNCLASSIFIED

## Login pages TODO
To inject this banner into the login pages:


## Admin console
To inject this banner into the admin console:

### Via ansible hosts variable during cluster deployment
```openshift_web_console_extension_script_urls=['https://banners.apps.example.com/banner.js']```
Note: the js file is served at /banner.js of the hostname you exposed with the route above.

### Via configmap change to an existing cluster
```oc edit configmap/webconsole-config -n openshift-web-console```
Edit the data.webconsole-config.yaml.clusterinfo.scriptURLs key to include your banner.js file reference.
```apiVersion: v1
kind: ConfigMap
data:
  webconsole-config.yaml: |
    apiVersion: webconsole.config.openshift.io/v1
    clusterInfo:
      [...]
      scriptURLs: "https://banners.apps.example.com/banner.js"
    [...]```
