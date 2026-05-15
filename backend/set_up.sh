#!/bin/bash

APP="news_app"

echo "Creating Django scalable structure..."

# =========================
# CREATE DIRECTORIES
# =========================

dirs=(
    "$APP/models"
    "$APP/views"
    "$APP/serializers"
    "$APP/services"
    "$APP/api/v1"
    "$APP/permissions"
    "$APP/tasks"
    "$APP/utils"
)

for dir in "${dirs[@]}"; do
    mkdir -p "$dir"
done

# =========================
# CREATE __init__.py FILES
# =========================

find "$APP" -type d | while read dir; do
    touch "$dir/__init__.py"
done

# =========================
# CREATE MODEL FILES
# =========================

model_files=(
    "article.py"
    "category.py"
    "tag.py"
    "player.py"
    "team.py"
    "fixture.py"
    "live_score.py"
    "video.py"
    "comment.py"
    "profile.py"
)

for file in "${model_files[@]}"; do
    touch "$APP/models/$file"
done

# =========================
# CREATE VIEW FILES
# =========================

view_files=(
    "article_views.py"
    "player_views.py"
    "team_views.py"
    "fixture_views.py"
    "live_views.py"
    "video_views.py"
    "auth_views.py"
)

for file in "${view_files[@]}"; do
    touch "$APP/views/$file"
done

# =========================
# CREATE SERIALIZER FILES
# =========================

serializer_files=(
    "article_serializer.py"
    "player_serializer.py"
    "team_serializer.py"
    "fixture_serializer.py"
    "live_score_serializer.py"
    "video_serializer.py"
)

for file in "${serializer_files[@]}"; do
    touch "$APP/serializers/$file"
done

# =========================
# CREATE SERVICE FILES
# =========================

service_files=(
    "article_service.py"
    "recommendation_service.py"
    "youtube_service.py"
    "live_score_service.py"
    "notification_service.py"
    "search_service.py"
)

for file in "${service_files[@]}"; do
    touch "$APP/services/$file"
done

# =========================
# CREATE API FILES
# =========================

api_files=(
    "urls.py"
)

for file in "${api_files[@]}"; do
    touch "$APP/api/$file"
done

api_v1_files=(
    "article_urls.py"
    "player_urls.py"
    "fixture_urls.py"
    "live_urls.py"
    "auth_urls.py"
)

for file in "${api_v1_files[@]}"; do
    touch "$APP/api/v1/$file"
done

# =========================
# CREATE PERMISSION FILES
# =========================

permission_files=(
    "is_editor.py"
    "is_admin.py"
    "is_author.py"
)

for file in "${permission_files[@]}"; do
    touch "$APP/permissions/$file"
done

# =========================
# CREATE TASK FILES
# =========================

task_files=(
    "fetch_live_scores.py"
    "fetch_youtube_videos.py"
    "send_notifications.py"
    "update_trending.py"
)

for file in "${task_files[@]}"; do
    touch "$APP/tasks/$file"
done

# =========================
# CREATE UTIL FILES
# =========================

util_files=(
    "helpers.py"
    "constants.py"
    "validators.py"
    "pagination.py"
    "slug_generator.py"
)

for file in "${util_files[@]}"; do
    touch "$APP/utils/$file"
done

# =========================
# MOVE EXISTING FILES
# =========================

# Move models.py
if [ -f "$APP/models.py" ]; then
    mv "$APP/models.py" "$APP/models/article.py"
    echo "Moved models.py -> models/article.py"
fi

# Move views.py
if [ -f "$APP/views.py" ]; then
    mv "$APP/views.py" "$APP/views/article_views.py"
    echo "Moved views.py -> views/article_views.py"
fi

echo "Done."
echo ""
echo "Next important step:"
echo "Update models/__init__.py imports."