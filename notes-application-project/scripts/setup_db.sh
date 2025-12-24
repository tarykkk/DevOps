#!/bin/bash

set -e

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m'

CONTAINER_NAME="${1:-notes_db_container}"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}   Database Initialization Script${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Load environment variables
if [ -f .env ]; then
    echo -e "${GREEN}✓ Loading environment variables...${NC}"
    export $(grep -v '^#' .env | xargs)
else
    echo -e "${YELLOW}⚠ No .env file found, using defaults${NC}"
fi

# Check if container is running
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo -e "${RED}✗ Container '${CONTAINER_NAME}' is not running${NC}"
    echo -e "${YELLOW}  Start containers with: docker-compose up -d${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Container '${CONTAINER_NAME}' is running${NC}"
echo ""

# Wait for database to be ready
echo -e "${YELLOW}⏳ Waiting for database to be ready...${NC}"
sleep 2

# Execute initialization script
echo -e "${YELLOW}📝 Executing SQL initialization...${NC}"
docker exec -i "${CONTAINER_NAME}" psql \\
    -U "${DB_USER:-postgres}" \\
    -d "${DB_NAME:-notesdb}" \\
    < database/init.sql

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Database initialized successfully!${NC}"
    echo ""
    
    # Show tables
    echo -e "${BLUE}📊 Database tables:${NC}"
    docker exec "${CONTAINER_NAME}" psql \\
        -U "${DB_USER:-postgres}" \\
        -d "${DB_NAME:-notesdb}" \\
        -c "\\dt"
    echo ""
    
    # Show sample data
    echo -e "${BLUE}📋 Sample notes:${NC}"
    docker exec "${CONTAINER_NAME}" psql \\
        -U "${DB_USER:-postgres}" \\
        -d "${DB_NAME:-notesdb}" \\
        -c "SELECT id, title, LEFT(content, 50) as preview FROM notes;"
else
    echo -e "${RED}✗ Database initialization failed${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   Setup completed successfully! ✓${NC}"
echo -e "${GREEN}========================================${NC}"