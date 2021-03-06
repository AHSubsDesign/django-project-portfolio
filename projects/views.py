from django.views import generic

from .models import Project, Version


class BaseProjectView(object):
    model = Project

    def get_queryset(self):
        return super(BaseProjectView, self).get_queryset().public()


class BaseVersionView(object):
    model = Version


class ProjectDetail(BaseProjectView, generic.DetailView):
    pass


class ProjectList(BaseProjectView, generic.ListView):
    pass


class VersionDetail(BaseVersionView, generic.DetailView):
    """
    Detail view of a specific Version of a Project.

    """
    project_url_kwarg = 'project_slug'
    slug_field = 'version'

    def get_object(self, queryset=None):
        """
        Returns the Version, doing the lookup through the Project
        (using an additional argument from the URL).

        """
        project_slug = self.kwargs.get(self.project_url_kwarg, None)
        if project_slug is None:
            raise AttributeError("VersionDetail must be called with "
                                 "a project slug.")
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(
            project__slug=project_slug,
            project__status=Project.PUBLIC_STATUS
        )
        return super(VersionDetail, self).get_object(queryset)


class LatestVersionsList(BaseVersionView, generic.ListView):
    """
    List view of the latest Version of each public Project, ordered by
    Project name.

    """
    template_name = 'projects/latest_versions.html'
    version_filter_kwargs = {
        'is_latest': True,
        'project__status': Project.PUBLIC_STATUS,
    }

    def get_queryset(self):
        queryset = super(LatestVersionsList, self).get_queryset()
        return queryset.filter(
            **self.version_filter_kwargs
            ).select_related('project').order_by('project')
