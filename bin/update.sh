set -e
cd /home/admin/day9
echo "Updating code..."
git fetch origin
git reset --hard origin/master

echo "Building new image..."
docker compose -f docker-compose.prod.yml build

echo "Deploying with rolling update..."
docker compose -f docker-compose.prod.yml up -d --no-deps --build

echo "Deployment successfull"