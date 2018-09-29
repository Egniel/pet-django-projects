echo 'Running npm build'
cd frontend && npm run build && cd ..
echo 'Done...Running npm build'

echo 'Copy vue index.html to templates and rename it to todo_vue.html'
mv 'frontend/index.html' 'templates/todo_vue.html'
echo 'Done...Copy index.html'

echo 'Collect static'
python manage.py collectstatic --noinput
echo 'Done...Collect static'

echo 'Restart gunicorn'
sudo systemctl restart gunicorn
echo 'Done...Restart gunicorn'

echo 'Restart nginx'
sudo nginx -t && sudo systemctl restart nginx
echo 'Done...Restart nginx'
