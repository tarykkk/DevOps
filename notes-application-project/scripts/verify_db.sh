#!/bin/bash

set -e

GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m'

CONTAINER_NAME="${1:-notes_db_container}"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}   Database Verification Report${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Load environment
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Check container status
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo -e "${RED}✗ Container is not running${NC}"
    exit 1
fi

DB_USER=${DB_USER:-postgres}
DB_NAME=${DB_NAME:-notesdb}

echo -e "${GREEN}✓ Container: ${CONTAINER_NAME}${NC}"
echo -e "${GREEN}✓ Database: ${DB_NAME}${NC}"
echo -e "${GREEN}✓ User: ${DB_USER}${NC}"
echo ""

# Connection test
echo -e "${YELLOW}🔌 Testing database connection...${NC}"
docker exec "${CONTAINER_NAME}" pg_isready -U "${DB_USER}" -d "${DB_NAME}"
echo ""

# Show table structure
echo -e "${YELLOW}📐 Table structure:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${DB_USER}" -d "${DB_NAME}" \\
    -c "\\d notes"
echo ""

# Count records
echo -e "${YELLOW}📊 Statistics:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${DB_USER}" -d "${DB_NAME}" \\
    -c "SELECT 
        COUNT(*) as total_notes,
        MIN(created_at) as oldest_note,
        MAX(created_at) as newest_note
    FROM notes;"
echo ""

# Show recent notes
echo -e "${YELLOW}📝 Recent notes (last 5):${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${DB_USER}" -d "${DB_NAME}" \\
    -c "SELECT 
        id, 
        title, 
        LEFT(content, 60) as content_preview,
        created_at 
    FROM notes 
    ORDER BY created_at DESC 
    LIMIT 5;"
echo ""

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   Verification completed! ✓${NC}"
echo -e "${GREEN}========================================${NC}"