#!/bin/bash

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${YELLOW}🧹 Cleaning up Docker resources...${NC}"
echo ""

# Stop containers
echo -e "${YELLOW}Stopping containers...${NC}"
docker-compose down

# Remove volumes (ask for confirmation)
read -p "Remove database volumes? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Removing volumes...${NC}"
    docker-compose down -v
    echo -e "${GREEN}✓ Volumes removed${NC}"
fi

# Remove orphaned images
echo -e "${YELLOW}Removing unused images...${NC}"
docker image prune -f

echo ""
echo -e "${GREEN}✓ Cleanup completed!${NC}"