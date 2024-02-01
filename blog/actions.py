from django.http import HttpResponse

from blog.utils import export_to_excel


def write_excel(name: str, queryset):
    file_path = ""
    if name == "PostAdmin":
        file_path = "db/posts.xlsx"
        posts = [
            [
                post.id,
                post.content,
                post.status,
                post.language,
                post.alternative.id,
                post.created_at.strftime("%d.%m.%Y %H:%M:%S"),
                post.updated_at.strftime("%d.%m.%Y %H:%M:%S"),
                post.previous(False).id if post.previous(False) else "",
                post.next(False).id if post.next(False) else "",
            ]
            for post in queryset
        ]

        export_to_excel(
            data=posts,
            headings=[
                "Post ID",
                "Content",
                "Status",
                "Language",
                "Alternative Post ID",
                "Created at",
                "Updated at",
                "Previous Post",
                "Next Post",
            ],
            filepath=file_path,
        )

    elif name == "AboutMeSectionsAdmin":
        file_path = "db/about_me_sections.xlsx"
        about_me_sections = [
            [
                section.meta,
                section.image,
                section.content,
                section.status,
                section.language,
                section.alternative.id,
            ]
            for section in queryset
        ]

        export_to_excel(
            data=about_me_sections,
            headings=[
                "Meta",
                "Image",
                "Content",
                "Status",
                "Language",
                "Alternative Section ID",
            ],
            filepath=file_path,
        )

    elif name == "CommentAdmin":
        file_path = "db/comments.xlsx"
        comments = [
            [
                comment.email,
                comment.content,
                comment.post.id,
                comment.reply_to.id if comment.reply_to else "",
                comment.created_at.strftime("%d.%m.%Y %H:%M:%S"),
                comment.updated_at.strftime("%d.%m.%Y %H:%M:%S"),
            ]
            for comment in queryset
        ]

        export_to_excel(
            data=comments,
            headings=[
                "Email",
                "Content",
                "Post ID",
                "Reply to ID",
                "Created at",
                "Updated at",
            ],
            filepath=file_path,
        )
    return file_path


def download_file(modeladmin, request, queryset):
    file_path = write_excel(modeladmin.__class__.__name__, queryset)

    with open(file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={file_path.split('/')[-1]}"
        return response
