source ../container-name.sh
IMAGE_NAME=$1

if [ $# -lt 1 ];
then
    echo "+ $0: Too few arguments!"
    echo "+ use something like:"
    echo "+ $0 <docker image>" 
    echo "+ $0 reslocal/${CONTAINER_NAME}"
    exit
fi

# remove currently running containers
echo "+ ID_TO_KILL=\$(docker ps -a -q  --filter ancestor=$1)"
ID_TO_KILL=$(docker ps -a -q  --filter ancestor=$1)

echo "+ docker ps -a"
docker ps -a
echo "+ docker stop ${ID_TO_KILL}"
docker stop ${ID_TO_KILL}
echo "+ docker rm -f ${ID_TO_KILL}"
docker rm -f ${ID_TO_KILL}
echo "+ docker ps -a"
docker ps -a

echo "dpcker run -v <dir-to-check-on-host>:/workdir -it --entrypoint /bin/sh ${IMAGE_NAME}"
echo "e.g.:"
echo "docker run -v /home/rber/projects/trainings/framework-3.0/intely-3.0:/workdir -it --entrypoint /bin/sh ${IMAGE_NAME}"
echo "docker run -v /home/student/projects/resy-playground/sources/meta-resy/recipes-example:/workdir -it --entrypoint /bin/sh ${IMAGE_NAME}"
