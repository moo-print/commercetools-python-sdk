# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import Environment

# Fields


# Marshmallow Schemas
class DataSourceConfigurationSchema(helpers.BaseSchema):
    data_source_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="dataSourceId"
    )
    type = marshmallow.fields.String(allow_none=True, load_default=None)
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    configuration = marshmallow.fields.Raw(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DataSourceConfiguration(**data)


class DataSourceResponseSchema(helpers.BaseSchema):
    data_source_payload = marshmallow.fields.Raw(
        allow_none=True, load_default=None, data_key="dataSourcePayload"
    )
    preview_payload = marshmallow.fields.Raw(
        allow_none=True, load_default=None, data_key="previewPayload"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DataSourceResponse(**data)


class DataSourcesSchema(helpers.BaseSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DataSources(**data)


class ErrorSchema(helpers.BaseSchema):
    ok = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    message = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Error(**data)


class FooterSchema(helpers.BaseSchema):
    layout_elements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LayoutElementSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="layoutElements",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Footer(**data)


class HeadSchema(helpers.BaseSchema):
    layout_elements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LayoutElementSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="layoutElements",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Head(**data)


class LayoutElementSchema(helpers.BaseSchema):
    layout_element_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="layoutElementId"
    )
    configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LayoutElementConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    tastics = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TasticSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LayoutElement(**data)


class LayoutElementConfigurationSchema(helpers.BaseSchema):
    size = marshmallow.fields.Float(allow_none=True, load_default=None)
    mobile = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    tablet = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    desktop = marshmallow.fields.Boolean(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LayoutElementConfiguration(**data)


class MainSchema(helpers.BaseSchema):
    layout_elements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LayoutElementSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="layoutElements",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Main(**data)


class PageSchema(helpers.BaseSchema):
    page_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="pageId"
    )
    sections = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SectionsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    state = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Page(**data)


class PageDataResponseSchema(helpers.BaseSchema):
    page_folder = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PageFolderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="pageFolder",
    )
    page = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PageSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ViewDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PageDataResponse(**data)


class PageFolderSchema(helpers.BaseSchema):
    page_folder_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="pageFolderId"
    )
    is_dynamic = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isDynamic"
    )
    page_folder_type = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="pageFolderType"
    )
    configuration = marshmallow.fields.Raw(allow_none=True, load_default=None)
    data_source_configurations = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DataSourceConfigurationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="dataSourceConfigurations",
    )
    name = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    ancestor_ids_materialized_path = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="ancestorIdsMaterializedPath"
    )
    depth = marshmallow.fields.Float(allow_none=True, load_default=None)
    sort = marshmallow.fields.Float(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PageFolder(**data)


class PagePreviewContextSchema(helpers.BaseSchema):
    customer_name = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="customerName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PagePreviewContext(**data)


class PagePreviewDataResponseSchema(PageDataResponseSchema):
    preview_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="previewId"
    )
    preview_context = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PagePreviewContextSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="previewContext",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PagePreviewDataResponse(**data)


class PathConfigurationSchema(helpers.BaseSchema):
    path = marshmallow.fields.String(allow_none=True, load_default=None)
    path_translations = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        load_default=None,
        data_key="pathTranslations",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PathConfiguration(**data)


class ProjectContextSchema(helpers.BaseSchema):
    environment = marshmallow_enum.EnumField(
        Environment, by_value=True, allow_none=True, load_default=None
    )
    locales = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )
    default_locale = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="defaultLocale"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProjectContext(**data)


class RedirectResponseSchema(helpers.BaseSchema):
    status_code = marshmallow.fields.Float(
        allow_none=True, load_default=None, data_key="statusCode"
    )
    reason = marshmallow.fields.String(allow_none=True, load_default=None)
    target_type = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="targetType"
    )
    target = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.RedirectResponse(**data)


class SectionsSchema(helpers.BaseSchema):
    head = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".HeadSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    main = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MainSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    footer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FooterSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Sections(**data)


class TasticSchema(helpers.BaseSchema):
    tastic_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="tasticId"
    )
    tastic_type = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="tasticType"
    )
    configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TasticConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Tastic(**data)


class TasticConfigurationSchema(helpers.BaseSchema):
    desktop = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    mobile = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    tablet = marshmallow.fields.Boolean(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TasticConfiguration(**data)


class ViewDataSchema(helpers.BaseSchema):
    data_sources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DataSourcesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="dataSources",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ViewData(**data)


class BuildUploadSchema(helpers.BaseSchema):
    metadata = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".BuildMetadataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    extension = marshmallow.fields.ToDo(allow_none=True, load_default=None)
    extension_map = marshmallow.fields.ToDo(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BuildUpload(**data)


class BuildMetadataSchema(helpers.BaseSchema):
    branch = marshmallow.fields.String(allow_none=True, load_default=None)
    revision = marshmallow.fields.String(allow_none=True, load_default=None)
    version_number = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="versionNumber"
    )
    node_js_version = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="nodeJsVersion",
    )
    build_successful = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="buildSuccessful"
    )
    build_time = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="buildTime"
    )
    build_duration = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="buildDuration"
    )
    build_log = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="buildLog"
    )
    deploy = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BuildMetadata(**data)


class BuildUploadResultSchema(helpers.BaseSchema):
    status = marshmallow.fields.String(allow_none=True, load_default=None)
    message = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BuildUploadResult(**data)
