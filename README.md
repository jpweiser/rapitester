# rapitester

This is a simple application intended for testing and demonstrating the (WIP) [rapidast-operator](https://github.com/RedHatProductSecurity/rapidast)

You will need [helm](https://helm.sh/docs/intro/install/) installed, as well as [OpenShift CLI](https://docs.openshift.com/container-platform/4.10/cli_reference/openshift_cli/getting-started-cli.html)(`oc`).

This document assumes both of these are already installed, that the user is logged into cluster, and that the user is using the project where the RapiDAST operator has already been installed. 


## Deploy Application
Install the application with the included helm chart.

```bash
helm install rapitester ./helm-chart
```

## Create RapiDAST Resource

After you have successfully deployed the application, apply the provided yaml to create an instance of a RapiDAST resource that is configured to scan the demo application. 

```bash
oc apply -f rapidast.yaml
```
