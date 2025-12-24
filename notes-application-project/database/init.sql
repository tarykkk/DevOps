-- Create notes table
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL CHECK (title <> ''),
    content TEXT NOT NULL CHECK (content <> ''),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster queries
CREATE INDEX IF NOT EXISTS idx_notes_created 
ON notes(created_at DESC);

-- Create index for title searches
CREATE INDEX IF NOT EXISTS idx_notes_title 
ON notes(title varchar_pattern_ops);

-- Function to automatically update updated_at timestamp
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to call the function
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON notes
FOR EACH ROW
EXECUTE FUNCTION trigger_set_timestamp();

-- Insert sample data
INSERT INTO notes (title, content) VALUES
    ('Getting Started', 'Welcome to the Notes application! This is a sample note to help you get started.'),
    ('Docker Setup', 'This application runs entirely in Docker containers with PostgreSQL database for data persistence.'),
    ('API Usage', 'Use POST /api/notes with JSON body to create notes. Use GET /api/notes to retrieve all notes.');

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON TABLE notes TO postgres;
GRANT USAGE, SELECT ON SEQUENCE notes_id_seq TO postgres;