from discount_scrapper.models import Course


class CourseService:

    @classmethod
    def list_course(cls, **wargs):
        return Course.objects.filter(**wargs).all()

    @classmethod
    def get_course(cls, **wargs):
        course = Course.objects.filter(**wargs).first()

        if not course:
            return None
        return course
