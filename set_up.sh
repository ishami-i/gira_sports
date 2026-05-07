#!/bin/bash

set -e

PROJECT_NAME= basename "$PWD"

echo "🚀 Creating full-stack project: $PROJECT_NAME"

# ---------------------------
# 1. Create root structure
# ---------------------------
mkdir -p $PROJECT_NAME
cd $PROJECT_NAME

mkdir -p backend frontend docs/{ERD,architecture,api,deployment}

echo "📁 Folders created"

# ---------------------------
# 2. Setup React (Vite + JS)
# ---------------------------
echo "⚛️ Creating React frontend with Vite..."

npm create vite@latest frontend -- --template react

cd frontend
npm install
cd ..

echo "✅ React frontend ready"

# ---------------------------
# 3. Setup Django backend
# ---------------------------
echo "🐍 Setting up Django backend..."

cd backend

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install django djangorestframework django-cors-headers

django-admin startproject config .

mkdir -p apps

cd ..

echo "✅ Django backend ready"

# ---------------------------
# 4. Move existing files if any
# ---------------------------
echo "📦 Organizing existing files..."

# If user already has loose files in root
for f in $(ls | grep -E '\.py$|\.js$|\.json$' 2>/dev/null); do
    if [[ $f == *.py ]]; then
        mv $f backend/ 2>/dev/null || true
    fi

    if [[ $f == *.js || $f == *.json ]]; then
        mv $f frontend/ 2>/dev/null || true
    fi
done

echo "📦 Files organized"

# ---------------------------
# 5. Create useful extras
# ---------------------------
touch README.md
touch .gitignore
touch docker-compose.yml

cat <<EOL > .gitignore
# Python
backend/venv/
__pycache__/

# Node
frontend/node_modules/
frontend/dist/

# Env
.env
EOL

echo "🧹 Cleanup done"

# ---------------------------
# 6. Final message
# ---------------------------
echo "🎉 Full-stack project setup complete!"
echo ""
echo "👉 Next steps:"
echo "   cd frontend && npm run dev"
echo "   cd backend && source venv/bin/activate && python manage.py runserver"