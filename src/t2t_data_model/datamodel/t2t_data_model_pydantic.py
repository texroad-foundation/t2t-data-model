from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'created_by': 'https://texroad.org',
     'default_prefix': 't2t',
     'default_range': 'string',
     'description': 'The Specifications fields (CDM-ID 400–660) of the Common Data '
                    'Model for Textile to Textile Recycling, and their values '
                    'lists.',
     'id': 'https://texroad-foundation.github.io/t2t-data-model/',
     'imports': ['linkml:types'],
     'in_language': 'en',
     'keywords': ['textile recycling',
                  'textile to textile',
                  'feedstock',
                  'specification',
                  'contaminant'],
     'license': 'https://creativecommons.org/licenses/by/4.0/',
     'name': 't2t_data_model',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  't2t': {'prefix_prefix': 't2t',
                          'prefix_reference': 'https://texroad-foundation.github.io/t2t-data-model/'}},
     'see_also': ['https://github.com/texroad-foundation/t2t-data-model'],
     'source_file': 'src/t2t_data_model/schema/t2t_data_model.yaml',
     'title': 'Common Data Model for Textile to Textile Recycling — Specifications'} )

class MaterialSource(str, Enum):
    Post_industrial = "post_industrial"
    """
    Textile waste from manufacturing, before products reach the market.
    """
    Pre_consumer = "pre_consumer"
    """
    Finished textile products that were never sold to consumers.
    """
    Post_consumer_Residential = "post_consumer_residential"
    """
    Textile waste discarded by individual households after consumer use.
    """
    Post_consumer_Commercial = "post_consumer_commercial"
    """
    Textile waste discarded after use by businesses such as hotels, hospitals, or offices.
    """


class ColorGeneric(str, Enum):
    Multicoloured = "multicoloured"
    Mostly_dark_colors = "mostly_dark_colors"
    Mostly_light_colors = "mostly_light_colors"
    Undyed = "undyed"
    White = "white"
    Indigo = "indigo"
    Red = "red"
    Pink = "pink"
    Orange = "orange"
    Yellow = "yellow"
    Green = "green"
    Blue = "blue"
    Brown = "brown"
    Grey = "grey"
    Purple = "purple"
    Navy = "navy"
    Other = "other"
    Black = "black"


class FiberCompositionName(str, Enum):
    Acrylic = "acrylic"
    Aramid = "aramid"
    Bamboo = "bamboo"
    Carbon = "carbon"
    Cashmere = "cashmere"
    Cotton = "cotton"
    Elastane = "elastane"
    Hemp = "hemp"
    Jute = "jute"
    Linen = "linen"
    Lyocell = "lyocell"
    Modal = "modal"
    Plant_fiber_LEFT_PARENTHESISotherRIGHT_PARENTHESIS = "plant_fiber_other"
    Polyamide = "polyamide"
    Polyamide_6 = "polyamide_6"
    Polyamide_66 = "polyamide_66"
    Polyester = "polyester"
    Silk = "silk"
    Viscose = "viscose"
    Wool = "wool"
    Other_animal_fibers = "other_animal_fibers"
    Other_cellulosic_fibers = "other_cellulosic_fibers"
    Other = "other"


class FiberCompositionThreshold(str, Enum):
    Minimum = "minimum"
    Maximum = "maximum"
    Amount_listed = "amount_listed"


class ContaminantType(str, Enum):
    Fibers = "fibers"
    Coatings_and_finishes = "coatings_and_finishes"
    Dyes_and_pigments = "dyes_and_pigments"
    Soft_trims_and_prints = "soft_trims_and_prints"
    Hard_trims = "hard_trims"
    Other_materials = "other_materials"


class ContaminantCoatingsAndFinishes(str, Enum):
    UV_resistant = "uv_resistant"
    Flame_retardant = "flame_retardant"
    Fire_resistant = "fire_resistant"
    Antimicrobial = "antimicrobial"
    Insect_repellent = "insect_repellent"
    Non_slipSOLIDUSdimensional_stability = "non_slip_dimensional_stability"
    Antistatic = "antistatic"
    Water_repellent = "water_repellent"
    Dirt_repellent = "dirt_repellent"
    Silicone = "silicone"
    Elastomeric = "elastomeric"
    Fabric_softening = "fabric_softening"
    Fabric_stiffness = "fabric_stiffness"
    Wrinkle_resistant = "wrinkle_resistant"
    Fabric_hand = "fabric_hand"
    Anti_pilling = "anti_pilling"
    Other = "other"


class ContaminantDyesAndPigments(str, Enum):
    Natural_dyes = "natural_dyes"
    Acid = "acid"
    Basic = "basic"
    Other = "other"


class ContaminantSoftTrimsAndPrints(str, Enum):
    Tape = "tape"
    Binding = "binding"
    Piping = "piping"
    LEFT_PARENTHESISFlagRIGHT_PARENTHESISlabel = "flag_label"
    Interlining = "interlining"
    Sewing_thread = "sewing_thread"
    Drawcord = "drawcord"
    Hook_AMPERSAND_loop_closure = "hook_and_loop_closure"
    Heat_transfer = "heat_transfer"
    Direct_screen_print = "direct_screen_print"
    Pigment_print = "pigment_print"
    Other = "other"


class ContaminantHardTrims(str, Enum):
    Button = "button"
    Snap_button = "snap_button"
    Cord_stopper = "cord_stopper"
    Aglet = "aglet"
    Metal_zip = "metal_zip"
    Plastic_zip = "plastic_zip"
    Puller = "puller"
    Hook_AMPERSAND_eye_closure = "hook_and_eye_closure"
    Buckle = "buckle"
    Rivet = "rivet"
    Studs = "studs"
    Sequins = "sequins"
    Other = "other"


class ContaminantOtherMaterials(str, Enum):
    Acrylic_LEFT_PARENTHESISpolymerRIGHT_PARENTHESIS = "acrylic_polymer"
    Silicone = "silicone"
    Polyacrylate = "polyacrylate"
    Polyvinyl_chloride = "polyvinyl_chloride"
    Polytetrafluoroethylene = "polytetrafluoroethylene"
    Polyoxymethylene = "polyoxymethylene"
    Acrylonitrile_butadiene_styrene = "acrylonitrile_butadiene_styrene"
    Aluminium = "aluminium"
    Brass = "brass"
    Zinc = "zinc"
    Stainless_steel = "stainless_steel"
    Copper = "copper"
    Ferrous_metal = "ferrous_metal"
    Non_ferrous_metal = "non_ferrous_metal"
    Polylactide = "polylactide"
    Polyethylene_furanoate = "polyethylene_furanoate"
    Aramid = "aramid"
    Carbon = "carbon"
    Glass = "glass"
    PFAS = "pfas"
    Other = "other"


class ContaminantAmountUnit(str, Enum):
    PERCENT_SIGN_of_total_batch_weight = "percent_of_total_batch_weight"
    PERCENT_SIGN_of_total_fiber_composition = "percent_of_total_fiber_composition"
    PPM = "ppm"


class ContaminantThreshold(str, Enum):
    Measured_value = "measured_value"
    Maximum = "maximum"
    Trace_amounts_accepted = "trace_amounts_accepted"
    Zero_tolerance = "zero_tolerance"


class ContaminantCheck(str, Enum):
    Not_evaluated = "not_evaluated"
    Detected = "detected"
    Not_detected = "not_detected"


class Format(str, Enum):
    Clippings = "clippings"
    """
    Produced by chopping or cutting textiles into smaller pieces during feedstock preparation
    """
    Cutting_waste = "cutting_waste"
    """
    Produced by manufacturers when cutting markers
    """
    DustSOLIDUSpowder = "dust_powder"
    Fiber = "fiber"
    Flakes = "flakes"
    Garments_SOLIDUS_linens_SOLIDUS_household_textiles = "garments_linens_household_textiles"
    Granules = "granules"
    Monomers = "monomers"
    Opened_fiber = "opened_fiber"
    """
    Textile that has been shredded or torn into fiber or a mix of fiber and pieces of textiles during feedstock preparation
    """
    Pellets = "pellets"
    Polymers = "polymers"
    Pulp = "pulp"
    Sliver = "sliver"
    Trim = "trim"
    Yarn = "yarn"
    Other = "other"


class PhysicalPropertyName(str, Enum):
    Brightness = "brightness"
    Crystallinity = "crystallinity"
    Degree_of_Polymerization_LEFT_PARENTHESISDPRIGHT_PARENTHESIS = "degree_of_polymerization_dp"
    Density = "density"
    Fiber_Length = "fiber_length"
    Intrinsic_Viscosity_LEFT_PARENTHESISIVRIGHT_PARENTHESIS = "intrinsic_viscosity_iv"
    MoistureSOLIDUSDry_Matter_Content = "moisture_dry_matter_content"
    Molecular_Weight_LEFT_PARENTHESISMwSOLIDUSMnRIGHT_PARENTHESIS = "molecular_weight_mw_mn"
    Piece_size = "piece_size"
    Rheology = "rheology"
    Thermal_Properties_LEFT_PARENTHESISTm_TgRIGHT_PARENTHESIS = "thermal_properties_tm_tg"
    Other = "other"


class PhysicalPropertyUnit(str, Enum):
    cm = "cm"
    INCREMENTE = "delta_e"
    mLSOLIDUSg = "ml_per_g"
    dLSOLIDUSg = "dl_per_g"
    gSOLIDUScmCIRCUMFLEX_ACCENT3 = "g_per_cm3"
    PERCENT_SIGN = "percent"


class FabricConstruction(str, Enum):
    Knit = "knit"
    Woven = "woven"
    Non_woven = "non_woven"
    Mixed_construction = "mixed_construction"


class YesNo(str, Enum):
    Yes = "yes"
    No = "no"



class Specification(ConfiguredBaseModel):
    """
    A batch's output specification or a technology's input requirements (CDM-ID 400 to 660).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://texroad-foundation.github.io/t2t-data-model/',
         'tree_root': True})

    material_sources: Optional[list[MaterialSource]] = Field(default=None, title="Material Source 1", description="""For input specifications, these terms define which streams the materials come from, including types of textile waste and other non-textile sources. If more than one source is used, this should be defined separately.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '400.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:material_sources'} })
    internal_product_name: Optional[str] = Field(default=None, title="Internal Product Name", description="""Written name, determined by the actor producing the outputs or the actor buying the inputs""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '500.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Alphanumeric text'},
                         'type': {'tag': 'type', 'value': 'Text'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:internal_product_name'} })
    color_generic: Optional[ColorGeneric] = Field(default=None, title="Color Generic", description="""Describes the color of the materials, mostly used for recycling feedstocks.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '510.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:color_generic'} })
    fiber_compositions: Optional[list[FiberComposition]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Specification']} })
    contaminants: Optional[list[Contaminant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Specification']} })
    format: Optional[Format] = Field(default=None, title="Format", description="""Describes the general shape of the materials to give context to measurements provided in Physical Properties fields.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:format'} })
    physical_properties: Optional[list[PhysicalProperty]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Specification']} })
    fabric_construction: Optional[FabricConstruction] = Field(default=None, title="Fabric Construction", description="""Used to describe finished products (garments and household textiles), some post-industrial waste (cuttings, off-cuts, rolled goods), clippings made during pre-processing, and other formats that include fabric pieces of any size""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.30'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:fabric_construction'} })
    recycled_content_in_outputs: Optional[YesNo] = Field(default=None, title="Recycled Content in Outputs", description="""For use on output batches. This should be determined based on the input materials used.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '650.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:recycled_content_in_outputs'} })
    recycled_contents: Optional[list[RecycledContent]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Specification']} })
    certificate_of_analysis: Optional[str] = Field(default=None, title="Certificate of Analysis", description="""For use on output batches. Should be provided to verify claims about specifications.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '660.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Document upload'},
                         'type': {'tag': 'type', 'value': 'Link to document'}},
         'domain_of': ['Specification'],
         'slot_uri': 't2t:certificate_of_analysis'} })


class FiberComposition(ConfiguredBaseModel):
    """
    One Fiber Composition entry, repeated as a group (the fields with a 1 in their name).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://texroad-foundation.github.io/t2t-data-model/'})

    fiber_composition_name: Optional[FiberCompositionName] = Field(default=None, title="Fiber Composition 1 Name", description="""Name of the desired or in-scope primary textile fiber or other material content (e.g. name of the monomer) according to a standardized list. Fibers that are a contaminant should be listed in Contaminants data fields. In the case that the primary in-scope material content is no longer textile, this data field is simply composition.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '520.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['FiberComposition'],
         'slot_uri': 't2t:fiber_composition_name'} })
    fiber_composition_value: Optional[Decimal] = Field(default=None, title="Fiber Composition 1 Value", description="""% of the total by weight for Fiber Composition 1 Name""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '520.10'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Number as a % (fixed format)'},
                         'type': {'tag': 'type', 'value': 'Percentage (0–100)'}},
         'domain_of': ['FiberComposition'],
         'slot_uri': 't2t:fiber_composition_value',
         'unit': {'symbol': '%'}} })
    fiber_composition_threshold: Optional[FiberCompositionThreshold] = Field(default=None, title="Fiber Composition 1 Threshold", description="""Describes how the numeric value in 520.10 should be applied - taken as a minimum, maximum, or absolute value""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '520.20'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['FiberComposition'],
         'slot_uri': 't2t:fiber_composition_threshold'} })


class Contaminant(ConfiguredBaseModel):
    """
    One Contaminant entry, repeated as a group (the fields with a 1 in their name).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://texroad-foundation.github.io/t2t-data-model/',
         'rules': [{'description': 'A Fibers contaminant is named from the Fiber '
                                   'Composition Name list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['acrylic',
                                                                                                     'aramid',
                                                                                                     'bamboo',
                                                                                                     'carbon',
                                                                                                     'cashmere',
                                                                                                     'cotton',
                                                                                                     'elastane',
                                                                                                     'hemp',
                                                                                                     'jute',
                                                                                                     'linen',
                                                                                                     'lyocell',
                                                                                                     'modal',
                                                                                                     'plant_fiber_other',
                                                                                                     'polyamide',
                                                                                                     'polyamide_6',
                                                                                                     'polyamide_66',
                                                                                                     'polyester',
                                                                                                     'silk',
                                                                                                     'viscose',
                                                                                                     'wool',
                                                                                                     'other_animal_fibers',
                                                                                                     'other_cellulosic_fibers',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'fibers',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A Coatings and finishes contaminant is named from '
                                   'the Contaminant Type > Coatings and finishes list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['uv_resistant',
                                                                                                     'flame_retardant',
                                                                                                     'fire_resistant',
                                                                                                     'antimicrobial',
                                                                                                     'insect_repellent',
                                                                                                     'non_slip_dimensional_stability',
                                                                                                     'antistatic',
                                                                                                     'water_repellent',
                                                                                                     'dirt_repellent',
                                                                                                     'silicone',
                                                                                                     'elastomeric',
                                                                                                     'fabric_softening',
                                                                                                     'fabric_stiffness',
                                                                                                     'wrinkle_resistant',
                                                                                                     'fabric_hand',
                                                                                                     'anti_pilling',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'coatings_and_finishes',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A Dyes and pigments contaminant is named from the '
                                   'Contaminant Type > Dyes and pigments list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['natural_dyes',
                                                                                                     'acid',
                                                                                                     'basic',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'dyes_and_pigments',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A Soft trims and prints contaminant is named from '
                                   'the Contaminant Type > Soft trims and prints list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['tape',
                                                                                                     'binding',
                                                                                                     'piping',
                                                                                                     'flag_label',
                                                                                                     'interlining',
                                                                                                     'sewing_thread',
                                                                                                     'drawcord',
                                                                                                     'hook_and_loop_closure',
                                                                                                     'heat_transfer',
                                                                                                     'direct_screen_print',
                                                                                                     'pigment_print',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'soft_trims_and_prints',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A Hard trims contaminant is named from the '
                                   'Contaminant Type > Hard trims list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['button',
                                                                                                     'snap_button',
                                                                                                     'cord_stopper',
                                                                                                     'aglet',
                                                                                                     'metal_zip',
                                                                                                     'plastic_zip',
                                                                                                     'puller',
                                                                                                     'hook_and_eye_closure',
                                                                                                     'buckle',
                                                                                                     'rivet',
                                                                                                     'studs',
                                                                                                     'sequins',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'hard_trims',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A Other materials contaminant is named from the '
                                   'Contaminant Type > Other materials list.',
                    'postconditions': {'slot_conditions': {'contaminant_name': {'equals_string_in': ['acrylic_polymer',
                                                                                                     'silicone',
                                                                                                     'polyacrylate',
                                                                                                     'polyvinyl_chloride',
                                                                                                     'polytetrafluoroethylene',
                                                                                                     'polyoxymethylene',
                                                                                                     'acrylonitrile_butadiene_styrene',
                                                                                                     'aluminium',
                                                                                                     'brass',
                                                                                                     'zinc',
                                                                                                     'stainless_steel',
                                                                                                     'copper',
                                                                                                     'ferrous_metal',
                                                                                                     'non_ferrous_metal',
                                                                                                     'polylactide',
                                                                                                     'polyethylene_furanoate',
                                                                                                     'aramid',
                                                                                                     'carbon',
                                                                                                     'glass',
                                                                                                     'pfas',
                                                                                                     'other'],
                                                                                'name': 'contaminant_name',
                                                                                'required': False}}},
                    'preconditions': {'slot_conditions': {'contaminant_type': {'equals_string': 'other_materials',
                                                                               'name': 'contaminant_type'}}}},
                   {'description': 'A hazardous substance needs its SDS and '
                                   'explanation (530.41, 530.42).',
                    'postconditions': {'slot_conditions': {'contaminant_explanation': {'name': 'contaminant_explanation',
                                                                                       'required': True},
                                                           'contaminant_sds': {'name': 'contaminant_sds',
                                                                               'required': True}}},
                    'preconditions': {'slot_conditions': {'contaminant_hazardous_substance': {'equals_string': 'yes',
                                                                                              'name': 'contaminant_hazardous_substance'}}}}]})

    contaminant_type: Optional[ContaminantType] = Field(default=None, title="Contaminant 1 Type", description="""Describes the functional type of the contaminant.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.00'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_type'} })
    contaminant_name: Optional[Union[ContaminantCoatingsAndFinishes, ContaminantDyesAndPigments, ContaminantHardTrims, ContaminantOtherMaterials, ContaminantSoftTrimsAndPrints, FiberCompositionName]] = Field(default=None, title="Contaminant 1 Name", description="""Describes the material the contaminant is made of.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.10'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'any_of': [{'range': 'FiberCompositionName'},
                    {'range': 'ContaminantCoatingsAndFinishes'},
                    {'range': 'ContaminantDyesAndPigments'},
                    {'range': 'ContaminantSoftTrimsAndPrints'},
                    {'range': 'ContaminantHardTrims'},
                    {'range': 'ContaminantOtherMaterials'}],
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_name'} })
    contaminant_amount: Optional[Decimal] = Field(default=None, title="Contaminant 1 Amount", description="""Numeric quantification of the Contaminant""", ge=0, json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.20'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Number (fixed format)'},
                         'type': {'tag': 'type',
                                  'value': 'Decimal number (0 or more)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_amount'} })
    contaminant_amount_unit: Optional[ContaminantAmountUnit] = Field(default=None, title="Contaminant 1 Amount Unit", description="""Unit of measure for numeric quantification of impurity amount or threshold amount (if numerically quantified)""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.21'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_amount_unit'} })
    contaminant_threshold: Optional[ContaminantThreshold] = Field(default=None, title="Contaminant 1 Threshold", description="""Defines control levels of the contaminant. This is used in a similar way as the threshold for fiber composition to clarify expectations of contaminant control for suppliers or buyers.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.22'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_threshold'} })
    contaminant_check: Optional[ContaminantCheck] = Field(default=None, title="Contaminant 1 Check", description="""Describes if the batch was checked on the presence of a certain contaminant.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.30'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_check'} })
    contaminant_hazardous_substance: Optional[YesNo] = Field(default=None, title="Contaminant 1 Hazardous Substance", description="""For output materials batches, this flags whether the contaminant appears on REACH restriction or candidate list. If this is \"yes\", SDS and a brief explanation of their use of potential presence in the material batch is required.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.40'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_hazardous_substance'} })
    contaminant_sds: Optional[str] = Field(default=None, title="Contaminant 1 SDS", description="""Upload SDS for hazardous chemical on REACH restriction or candidate list. Required when Contaminant Hazard is marked \"yes\".""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.41'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Document upload'},
                         'type': {'tag': 'type', 'value': 'Link to document'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_sds'} })
    contaminant_explanation: Optional[str] = Field(default=None, title="Contaminant 1 Explanation", description="""Brief explanation of use of or contact with hazardous chemical on REACH restriction or candidate list. Required when Contaminant Hazard is marked \"yes\".""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.42'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Open text (multi-line)'},
                         'type': {'tag': 'type', 'value': 'Text (multi-line)'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_explanation'} })
    contaminant_evidence: Optional[str] = Field(default=None, title="Contaminant 1 Evidence", description="""Upload evidence to support claims related to explanation of hazardous substances.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '530.43'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Document upload'},
                         'type': {'tag': 'type', 'value': 'Link to document'}},
         'domain_of': ['Contaminant'],
         'slot_uri': 't2t:contaminant_evidence'} })


class PhysicalProperty(ConfiguredBaseModel):
    """
    One Physical Property entry, repeated as a group (the fields with a 1 in their name).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://texroad-foundation.github.io/t2t-data-model/'})

    physical_property_name: Optional[PhysicalPropertyName] = Field(default=None, title="Physical Property 1 Name", description="""Describes measurable characteristics that are quantified in additional data fields.
This has a very, very broad application (e.g. fiber length, fabric width, viscosity, brightness)""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.10'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['PhysicalProperty'],
         'slot_uri': 't2t:physical_property_name'} })
    physical_property_value: Optional[Decimal] = Field(default=None, title="Physical Property 1 Value", description="""Numerical value used to measure Physical Property""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.20'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Number (fixed format)'},
                         'type': {'tag': 'type', 'value': 'Decimal number'}},
         'domain_of': ['PhysicalProperty'],
         'slot_uri': 't2t:physical_property_value'} })
    physical_property_unit: Optional[PhysicalPropertyUnit] = Field(default=None, title="Physical Property 1 Unit", description="""Unit of the numerical value used for Physical Property Value.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.21'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['PhysicalProperty'],
         'slot_uri': 't2t:physical_property_unit'} })
    physical_property_verification_method: Optional[str] = Field(default=None, title="Physical Property 1 Verification Method", description="""Equipment or testing method used to measure Physical Property""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '600.22'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Open text (multi-line)'},
                         'type': {'tag': 'type', 'value': 'Text (multi-line)'}},
         'domain_of': ['PhysicalProperty'],
         'slot_uri': 't2t:physical_property_verification_method'} })


class RecycledContent(ConfiguredBaseModel):
    """
    One Recycled Content entry, repeated as a group (the fields with a 1 in their name).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://texroad-foundation.github.io/t2t-data-model/'})

    recycled_content_source: Optional[MaterialSource] = Field(default=None, title="Recycled Content 1 Source", description="""For use on output batches. This should be determined based on the input materials used.""", json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '650.10'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Text (from values list)'},
                         'type': {'tag': 'type', 'value': 'Code (from values list)'}},
         'domain_of': ['RecycledContent'],
         'slot_uri': 't2t:recycled_content_source'} })
    recycled_content_value: Optional[Decimal] = Field(default=None, title="Recycled Content 1 Value", description="""Quantifies the amount of recycled content by percentage of total weight. If multiple recycled content sources are used, this data should be provided separately in individual lines.""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'annotations': {'cdm_id': {'tag': 'cdm_id', 'value': '650.20'},
                         'data_format': {'tag': 'data_format',
                                         'value': 'Number (fixed format)'},
                         'type': {'tag': 'type', 'value': 'Percentage (0–100)'}},
         'domain_of': ['RecycledContent'],
         'slot_uri': 't2t:recycled_content_value',
         'unit': {'symbol': '%'}} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Specification.model_rebuild()
FiberComposition.model_rebuild()
Contaminant.model_rebuild()
PhysicalProperty.model_rebuild()
RecycledContent.model_rebuild()
