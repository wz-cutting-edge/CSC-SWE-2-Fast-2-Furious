@echo off
start cmd /k "cd archive_backend && python manage.py runserver"
start cmd /k "cd library-archive && npm run dev"