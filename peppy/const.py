""" Package constants """

__author__ = "Michal Stolarczyk"
__email__ = "michal@virginia.edu"

# Project-related
NAME_KEY = "name"
CONFIG_VERSION_KEY = "pep_version"
DESC_KEY = "description"
CONFIG_FILE_KEY = "_config_file"
SAMPLE_TABLE_FILE_KEY = "_sample_table_path"
SUBSAMPLE_TABLES_FILE_KEY = "_subsample_tables_path"
SAMPLE_TABLE_INDEX_KEY = "sample_table_index"
SUBSAMPLE_TABLE_INDEX_KEY = "subsample_table_index"
CONFIG_KEY = "_config"
PROJECT_TYPENAME = "Project"
SAMPLE_MODS_KEY = "sample_modifiers"
PROJ_MODS_KEY = "project_modifiers"
NAME_TABLE_ATTR = "sample_table"
CONSTANT_KEY = "append"
REMOVE_KEY = "remove"
DUPLICATED_KEY = "duplicate"
DERIVED_KEY = "derive"
DERIVED_SOURCES_KEY = "sources"
DERIVED_ATTRS_KEY = "attributes"
IMPLIED_KEY = "imply"
IMPLIED_THEN_KEY = "then"
IMPLIED_IF_KEY = "if"
IMPLIED_COND_KEYS = [IMPLIED_IF_KEY, IMPLIED_THEN_KEY]
METADATA_KEY = "metadata"
OUTDIR_KEY = "output_dir"
CFG_IMPORTS_KEY = "import"
AMENDMENTS_KEY = "amend"
ACTIVE_AMENDMENTS_KEY = "_" + AMENDMENTS_KEY
SAMPLE_EDIT_FLAG_KEY = "_samples_touched"
SAMPLE_MODIFIERS = [CONSTANT_KEY, IMPLIED_KEY, DERIVED_KEY, DUPLICATED_KEY, REMOVE_KEY]
PROJECT_MODIFIERS = [CFG_IMPORTS_KEY, AMENDMENTS_KEY]
PROJECT_CONSTANTS = [
    "REQUIRED_VERSION",
    "CONSTANT_KEY",
    "DERIVED_SOURCES_KEY",
    "DERIVED_KEY",
    "SAMPLE_MODS_KEY",
    "IMPLIED_KEY",
    "METADATA_KEY",
    "NAME_TABLE_ATTR",
    "OUTDIR_KEY",
    "CONFIG_FILE_KEY",
    "SAMPLE_TABLE_FILE_KEY",
    "SUBSAMPLE_TABLES_FILE_KEY",
    "SAMPLE_TABLE_INDEX_KEY",
    "SUBSAMPLE_TABLE_INDEX_KEY",
    "CONFIG_KEY",
    "NAME_KEY",
    "REMOVE_KEY",
    "AMENDMENTS_KEY",
    "PROJECT_TYPENAME",
    "SAMPLE_MODS_KEY",
    "CONFIG_VERSION_KEY",
    "DUPLICATED_KEY",
    "SAMPLE_EDIT_FLAG_KEY",
    "CFG_IMPORTS_KEY",
    "ACTIVE_AMENDMENTS_KEY",
    "DERIVED_ATTRS_KEY",
    "IMPLIED_COND_KEYS",
    "IMPLIED_IF_KEY",
    "IMPLIED_THEN_KEY",
    "PROJ_MODS_KEY",
    "PROJECT_MODIFIERS",
    "DESC_KEY",
]

# Sample-related
SAMPLE_YAML_FILE_KEY = "yaml_file"
SAMPLE_YAML_EXT = (".yaml", ".yml")
SAMPLE_NAME_ATTR = "sample_name"
SUBSAMPLE_NAME_ATTR = "subsample_name"
SAMPLE_SHEET_KEY = "sample_sheet"
SUBSAMPLE_SHEET_KEY = "subsample_sheet"
CFG_SAMPLE_TABLE_KEY = "sample_table"
CFG_SUBSAMPLE_TABLE_KEY = "subsample_table"
SAMPLE_DF_KEY = "_sample_df"
SUBSAMPLE_DF_KEY = "_subsample_df"
SAMPLE_DF_LARGE = "_large_sample_df"
PRJ_REF = "_project"
ATTR_KEY_PREFIX = "_key_"
INPUTS_ATTR_NAME = "input_attrs"
REQ_INPUTS_ATTR_NAME = "required_" + INPUTS_ATTR_NAME
PROTOCOL_KEY = "protocol"
SAMPLE_CONSTANTS = [
    "PROTOCOL_KEY",
    "SUBSAMPLE_SHEET_KEY",
    "SAMPLE_SHEET_KEY",
    "PRJ_REF",
    "SAMPLE_NAME_ATTR",
    "ATTR_KEY_PREFIX",
    "CFG_SAMPLE_TABLE_KEY",
    "CFG_SUBSAMPLE_TABLE_KEY",
    "SAMPLE_DF_KEY",
    "SUBSAMPLE_DF_KEY",
    "SAMPLE_DF_LARGE",
    "SUBSAMPLE_NAME_ATTR",
    "INPUTS_ATTR_NAME",
    "REQ_INPUTS_ATTR_NAME",
    "SAMPLE_YAML_FILE_KEY",
    "SAMPLE_YAML_EXT",
    "SAMPLE_MODIFIERS",
]

# Other
REQUIRED_VERSION = ["2", "1", "0"]
PKG_NAME = "peppy"
MAX_PROJECT_SAMPLES_REPR = 20
OTHER_CONSTANTS = [
    "MAX_PROJECT_SAMPLES_REPR",
    "PKG_NAME",
    "REQUIRED_VERSION",
]


__all__ = PROJECT_CONSTANTS + SAMPLE_CONSTANTS + OTHER_CONSTANTS
