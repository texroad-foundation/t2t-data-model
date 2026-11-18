# Auto generated from t2t_data_model.yaml by pythongen.py version: 0.0.1
# Schema: t2t_data_model
#
# id: https://texroad-foundation.github.io/t2t-data-model/
# description: The Specifications fields (CDM-ID 400–660) of the Common Data Model for Textile to Textile Recycling, and their values lists.
# license: https://creativecommons.org/licenses/by/4.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Decimal, String, Uri
from linkml_runtime.utils.metamodelcore import Decimal, URI

metamodel_version = "1.12.0"
version = "0.1.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
T2T = CurieNamespace('t2t', 'https://texroad-foundation.github.io/t2t-data-model/')
DEFAULT_ = T2T


# Types

# Class references



@dataclass(repr=False)
class Specification(YAMLRoot):
    """
    A batch's output specification or a technology's input requirements (CDM-ID 400 to 660).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = T2T["Specification"]
    class_class_curie: ClassVar[str] = "t2t:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = T2T.Specification

    material_sources: Optional[Union[Union[str, "MaterialSource"], list[Union[str, "MaterialSource"]]]] = empty_list()
    internal_product_name: Optional[str] = None
    color_generic: Optional[Union[str, "ColorGeneric"]] = None
    fiber_compositions: Optional[Union[Union[dict, "FiberComposition"], list[Union[dict, "FiberComposition"]]]] = empty_list()
    contaminants: Optional[Union[Union[dict, "Contaminant"], list[Union[dict, "Contaminant"]]]] = empty_list()
    format: Optional[Union[str, "Format"]] = None
    physical_properties: Optional[Union[Union[dict, "PhysicalProperty"], list[Union[dict, "PhysicalProperty"]]]] = empty_list()
    fabric_construction: Optional[Union[str, "FabricConstruction"]] = None
    recycled_content_in_outputs: Optional[Union[str, "YesNo"]] = None
    recycled_contents: Optional[Union[Union[dict, "RecycledContent"], list[Union[dict, "RecycledContent"]]]] = empty_list()
    certificate_of_analysis: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_sources, list):
            self.material_sources = [self.material_sources] if self.material_sources is not None else []
        self.material_sources = [v if isinstance(v, MaterialSource) else MaterialSource(v) for v in self.material_sources]

        if self.internal_product_name is not None and not isinstance(self.internal_product_name, str):
            self.internal_product_name = str(self.internal_product_name)

        if self.color_generic is not None and not isinstance(self.color_generic, ColorGeneric):
            self.color_generic = ColorGeneric(self.color_generic)

        if not isinstance(self.fiber_compositions, list):
            self.fiber_compositions = [self.fiber_compositions] if self.fiber_compositions is not None else []
        self.fiber_compositions = [v if isinstance(v, FiberComposition) else FiberComposition(**as_dict(v)) for v in self.fiber_compositions]

        if not isinstance(self.contaminants, list):
            self.contaminants = [self.contaminants] if self.contaminants is not None else []
        self.contaminants = [v if isinstance(v, Contaminant) else Contaminant(**as_dict(v)) for v in self.contaminants]

        if self.format is not None and not isinstance(self.format, Format):
            self.format = Format(self.format)

        if not isinstance(self.physical_properties, list):
            self.physical_properties = [self.physical_properties] if self.physical_properties is not None else []
        self.physical_properties = [v if isinstance(v, PhysicalProperty) else PhysicalProperty(**as_dict(v)) for v in self.physical_properties]

        if self.fabric_construction is not None and not isinstance(self.fabric_construction, FabricConstruction):
            self.fabric_construction = FabricConstruction(self.fabric_construction)

        if self.recycled_content_in_outputs is not None and not isinstance(self.recycled_content_in_outputs, YesNo):
            self.recycled_content_in_outputs = YesNo(self.recycled_content_in_outputs)

        if not isinstance(self.recycled_contents, list):
            self.recycled_contents = [self.recycled_contents] if self.recycled_contents is not None else []
        self.recycled_contents = [v if isinstance(v, RecycledContent) else RecycledContent(**as_dict(v)) for v in self.recycled_contents]

        if self.certificate_of_analysis is not None and not isinstance(self.certificate_of_analysis, URI):
            self.certificate_of_analysis = URI(self.certificate_of_analysis)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FiberComposition(YAMLRoot):
    """
    One Fiber Composition entry, repeated as a group (the fields with a 1 in their name).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = T2T["FiberComposition"]
    class_class_curie: ClassVar[str] = "t2t:FiberComposition"
    class_name: ClassVar[str] = "FiberComposition"
    class_model_uri: ClassVar[URIRef] = T2T.FiberComposition

    fiber_composition_name: Optional[Union[str, "FiberCompositionName"]] = None
    fiber_composition_value: Optional[Decimal] = None
    fiber_composition_threshold: Optional[Union[str, "FiberCompositionThreshold"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fiber_composition_name is not None and not isinstance(self.fiber_composition_name, FiberCompositionName):
            self.fiber_composition_name = FiberCompositionName(self.fiber_composition_name)

        if self.fiber_composition_value is not None and not isinstance(self.fiber_composition_value, Decimal):
            self.fiber_composition_value = Decimal(self.fiber_composition_value)

        if self.fiber_composition_threshold is not None and not isinstance(self.fiber_composition_threshold, FiberCompositionThreshold):
            self.fiber_composition_threshold = FiberCompositionThreshold(self.fiber_composition_threshold)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contaminant(YAMLRoot):
    """
    One Contaminant entry, repeated as a group (the fields with a 1 in their name).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = T2T["Contaminant"]
    class_class_curie: ClassVar[str] = "t2t:Contaminant"
    class_name: ClassVar[str] = "Contaminant"
    class_model_uri: ClassVar[URIRef] = T2T.Contaminant

    contaminant_type: Optional[Union[str, "ContaminantType"]] = None
    contaminant_name: Optional[Union[str, "FiberCompositionName", "ContaminantCoatingsAndFinishes", "ContaminantDyesAndPigments", "ContaminantSoftTrimsAndPrints", "ContaminantHardTrims", "ContaminantOtherMaterials"]] = None
    contaminant_amount: Optional[Decimal] = None
    contaminant_amount_unit: Optional[Union[str, "ContaminantAmountUnit"]] = None
    contaminant_threshold: Optional[Union[str, "ContaminantThreshold"]] = None
    contaminant_check: Optional[Union[str, "ContaminantCheck"]] = None
    contaminant_hazardous_substance: Optional[Union[str, "YesNo"]] = None
    contaminant_sds: Optional[Union[str, URI]] = None
    contaminant_explanation: Optional[str] = None
    contaminant_evidence: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contaminant_type is not None and not isinstance(self.contaminant_type, ContaminantType):
            self.contaminant_type = ContaminantType(self.contaminant_type)

        if self.contaminant_name is not None and not isinstance(self.contaminant_name, (FiberCompositionName, ContaminantCoatingsAndFinishes, ContaminantDyesAndPigments, ContaminantSoftTrimsAndPrints, ContaminantHardTrims, ContaminantOtherMaterials)):
            value = self.contaminant_name
            for _coerce in (lambda: FiberCompositionName(value), lambda: ContaminantCoatingsAndFinishes(value), lambda: ContaminantDyesAndPigments(value), lambda: ContaminantSoftTrimsAndPrints(value), lambda: ContaminantHardTrims(value), lambda: ContaminantOtherMaterials(value)):
                try:
                    self.contaminant_name = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[FiberCompositionName, ContaminantCoatingsAndFinishes, ContaminantDyesAndPigments, ContaminantSoftTrimsAndPrints, ContaminantHardTrims, ContaminantOtherMaterials] could be constructed from {value!r} for slot contaminant_name")

        if self.contaminant_amount is not None and not isinstance(self.contaminant_amount, Decimal):
            self.contaminant_amount = Decimal(self.contaminant_amount)

        if self.contaminant_amount_unit is not None and not isinstance(self.contaminant_amount_unit, ContaminantAmountUnit):
            self.contaminant_amount_unit = ContaminantAmountUnit(self.contaminant_amount_unit)

        if self.contaminant_threshold is not None and not isinstance(self.contaminant_threshold, ContaminantThreshold):
            self.contaminant_threshold = ContaminantThreshold(self.contaminant_threshold)

        if self.contaminant_check is not None and not isinstance(self.contaminant_check, ContaminantCheck):
            self.contaminant_check = ContaminantCheck(self.contaminant_check)

        if self.contaminant_hazardous_substance is not None and not isinstance(self.contaminant_hazardous_substance, YesNo):
            self.contaminant_hazardous_substance = YesNo(self.contaminant_hazardous_substance)

        if self.contaminant_sds is not None and not isinstance(self.contaminant_sds, URI):
            self.contaminant_sds = URI(self.contaminant_sds)

        if self.contaminant_explanation is not None and not isinstance(self.contaminant_explanation, str):
            self.contaminant_explanation = str(self.contaminant_explanation)

        if self.contaminant_evidence is not None and not isinstance(self.contaminant_evidence, URI):
            self.contaminant_evidence = URI(self.contaminant_evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalProperty(YAMLRoot):
    """
    One Physical Property entry, repeated as a group (the fields with a 1 in their name).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = T2T["PhysicalProperty"]
    class_class_curie: ClassVar[str] = "t2t:PhysicalProperty"
    class_name: ClassVar[str] = "PhysicalProperty"
    class_model_uri: ClassVar[URIRef] = T2T.PhysicalProperty

    physical_property_name: Optional[Union[str, "PhysicalPropertyName"]] = None
    physical_property_value: Optional[Decimal] = None
    physical_property_unit: Optional[Union[str, "PhysicalPropertyUnit"]] = None
    physical_property_verification_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.physical_property_name is not None and not isinstance(self.physical_property_name, PhysicalPropertyName):
            self.physical_property_name = PhysicalPropertyName(self.physical_property_name)

        if self.physical_property_value is not None and not isinstance(self.physical_property_value, Decimal):
            self.physical_property_value = Decimal(self.physical_property_value)

        if self.physical_property_unit is not None and not isinstance(self.physical_property_unit, PhysicalPropertyUnit):
            self.physical_property_unit = PhysicalPropertyUnit(self.physical_property_unit)

        if self.physical_property_verification_method is not None and not isinstance(self.physical_property_verification_method, str):
            self.physical_property_verification_method = str(self.physical_property_verification_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecycledContent(YAMLRoot):
    """
    One Recycled Content entry, repeated as a group (the fields with a 1 in their name).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = T2T["RecycledContent"]
    class_class_curie: ClassVar[str] = "t2t:RecycledContent"
    class_name: ClassVar[str] = "RecycledContent"
    class_model_uri: ClassVar[URIRef] = T2T.RecycledContent

    recycled_content_source: Optional[Union[str, "MaterialSource"]] = None
    recycled_content_value: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.recycled_content_source is not None and not isinstance(self.recycled_content_source, MaterialSource):
            self.recycled_content_source = MaterialSource(self.recycled_content_source)

        if self.recycled_content_value is not None and not isinstance(self.recycled_content_value, Decimal):
            self.recycled_content_value = Decimal(self.recycled_content_value)

        super().__post_init__(**kwargs)


# Enumerations
class MaterialSource(EnumDefinitionImpl):

    post_industrial = PermissibleValue(
        text="post_industrial",
        title="Post-industrial",
        description="Textile waste from manufacturing, before products reach the market.",
        meaning=T2T["lists/material_source/post_industrial"])
    pre_consumer = PermissibleValue(
        text="pre_consumer",
        title="Pre-consumer",
        description="Finished textile products that were never sold to consumers.",
        meaning=T2T["lists/material_source/pre_consumer"])
    post_consumer_residential = PermissibleValue(
        text="post_consumer_residential",
        title="Post-consumer, Residential",
        description="Textile waste discarded by individual households after consumer use.",
        meaning=T2T["lists/material_source/post_consumer_residential"])
    post_consumer_commercial = PermissibleValue(
        text="post_consumer_commercial",
        title="Post-consumer, Commercial",
        description="Textile waste discarded after use by businesses such as hotels, hospitals, or offices.",
        meaning=T2T["lists/material_source/post_consumer_commercial"])

    _defn = EnumDefinition(
        name="MaterialSource",
    )

class ColorGeneric(EnumDefinitionImpl):

    multicoloured = PermissibleValue(
        text="multicoloured",
        title="Multicoloured",
        meaning=T2T["lists/color_generic/multicoloured"])
    mostly_dark_colors = PermissibleValue(
        text="mostly_dark_colors",
        title="Mostly dark colors",
        meaning=T2T["lists/color_generic/mostly_dark_colors"])
    mostly_light_colors = PermissibleValue(
        text="mostly_light_colors",
        title="Mostly light colors",
        meaning=T2T["lists/color_generic/mostly_light_colors"])
    undyed = PermissibleValue(
        text="undyed",
        title="Undyed",
        meaning=T2T["lists/color_generic/undyed"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=T2T["lists/color_generic/white"])
    indigo = PermissibleValue(
        text="indigo",
        title="Indigo",
        meaning=T2T["lists/color_generic/indigo"])
    red = PermissibleValue(
        text="red",
        title="Red",
        meaning=T2T["lists/color_generic/red"])
    pink = PermissibleValue(
        text="pink",
        title="Pink",
        meaning=T2T["lists/color_generic/pink"])
    orange = PermissibleValue(
        text="orange",
        title="Orange",
        meaning=T2T["lists/color_generic/orange"])
    yellow = PermissibleValue(
        text="yellow",
        title="Yellow",
        meaning=T2T["lists/color_generic/yellow"])
    green = PermissibleValue(
        text="green",
        title="Green",
        meaning=T2T["lists/color_generic/green"])
    blue = PermissibleValue(
        text="blue",
        title="Blue",
        meaning=T2T["lists/color_generic/blue"])
    brown = PermissibleValue(
        text="brown",
        title="Brown",
        meaning=T2T["lists/color_generic/brown"])
    grey = PermissibleValue(
        text="grey",
        title="Grey",
        meaning=T2T["lists/color_generic/grey"])
    purple = PermissibleValue(
        text="purple",
        title="Purple",
        meaning=T2T["lists/color_generic/purple"])
    navy = PermissibleValue(
        text="navy",
        title="Navy",
        meaning=T2T["lists/color_generic/navy"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/color_generic/other"])
    black = PermissibleValue(
        text="black",
        title="Black",
        meaning=T2T["lists/color_generic/black"])

    _defn = EnumDefinition(
        name="ColorGeneric",
    )

class FiberCompositionName(EnumDefinitionImpl):

    acrylic = PermissibleValue(
        text="acrylic",
        title="Acrylic",
        meaning=T2T["lists/fiber_composition_name/acrylic"])
    aramid = PermissibleValue(
        text="aramid",
        title="Aramid",
        meaning=T2T["lists/fiber_composition_name/aramid"])
    bamboo = PermissibleValue(
        text="bamboo",
        title="Bamboo",
        meaning=T2T["lists/fiber_composition_name/bamboo"])
    carbon = PermissibleValue(
        text="carbon",
        title="Carbon",
        meaning=T2T["lists/fiber_composition_name/carbon"])
    cashmere = PermissibleValue(
        text="cashmere",
        title="Cashmere",
        meaning=T2T["lists/fiber_composition_name/cashmere"])
    cotton = PermissibleValue(
        text="cotton",
        title="Cotton",
        meaning=T2T["lists/fiber_composition_name/cotton"])
    elastane = PermissibleValue(
        text="elastane",
        title="Elastane",
        meaning=T2T["lists/fiber_composition_name/elastane"])
    hemp = PermissibleValue(
        text="hemp",
        title="Hemp",
        meaning=T2T["lists/fiber_composition_name/hemp"])
    jute = PermissibleValue(
        text="jute",
        title="Jute",
        meaning=T2T["lists/fiber_composition_name/jute"])
    linen = PermissibleValue(
        text="linen",
        title="Linen",
        meaning=T2T["lists/fiber_composition_name/linen"])
    lyocell = PermissibleValue(
        text="lyocell",
        title="Lyocell",
        meaning=T2T["lists/fiber_composition_name/lyocell"])
    modal = PermissibleValue(
        text="modal",
        title="Modal",
        meaning=T2T["lists/fiber_composition_name/modal"])
    plant_fiber_other = PermissibleValue(
        text="plant_fiber_other",
        title="Plant fiber (other)",
        meaning=T2T["lists/fiber_composition_name/plant_fiber_other"])
    polyamide = PermissibleValue(
        text="polyamide",
        title="Polyamide",
        meaning=T2T["lists/fiber_composition_name/polyamide"])
    polyamide_6 = PermissibleValue(
        text="polyamide_6",
        title="Polyamide 6",
        meaning=T2T["lists/fiber_composition_name/polyamide_6"])
    polyamide_66 = PermissibleValue(
        text="polyamide_66",
        title="Polyamide 66",
        meaning=T2T["lists/fiber_composition_name/polyamide_66"])
    polyester = PermissibleValue(
        text="polyester",
        title="Polyester",
        meaning=T2T["lists/fiber_composition_name/polyester"])
    silk = PermissibleValue(
        text="silk",
        title="Silk",
        meaning=T2T["lists/fiber_composition_name/silk"])
    viscose = PermissibleValue(
        text="viscose",
        title="Viscose",
        meaning=T2T["lists/fiber_composition_name/viscose"])
    wool = PermissibleValue(
        text="wool",
        title="Wool",
        meaning=T2T["lists/fiber_composition_name/wool"])
    other_animal_fibers = PermissibleValue(
        text="other_animal_fibers",
        title="Other animal fibers",
        meaning=T2T["lists/fiber_composition_name/other_animal_fibers"])
    other_cellulosic_fibers = PermissibleValue(
        text="other_cellulosic_fibers",
        title="Other cellulosic fibers",
        meaning=T2T["lists/fiber_composition_name/other_cellulosic_fibers"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/fiber_composition_name/other"])

    _defn = EnumDefinition(
        name="FiberCompositionName",
    )

class FiberCompositionThreshold(EnumDefinitionImpl):

    minimum = PermissibleValue(
        text="minimum",
        title="Minimum",
        meaning=T2T["lists/fiber_composition_threshold/minimum"])
    maximum = PermissibleValue(
        text="maximum",
        title="Maximum",
        meaning=T2T["lists/fiber_composition_threshold/maximum"])
    amount_listed = PermissibleValue(
        text="amount_listed",
        title="Amount listed",
        meaning=T2T["lists/fiber_composition_threshold/amount_listed"])

    _defn = EnumDefinition(
        name="FiberCompositionThreshold",
    )

class ContaminantType(EnumDefinitionImpl):

    fibers = PermissibleValue(
        text="fibers",
        title="Fibers",
        meaning=T2T["lists/contaminant_type/fibers"])
    coatings_and_finishes = PermissibleValue(
        text="coatings_and_finishes",
        title="Coatings and finishes",
        meaning=T2T["lists/contaminant_type/coatings_and_finishes"])
    dyes_and_pigments = PermissibleValue(
        text="dyes_and_pigments",
        title="Dyes and pigments",
        meaning=T2T["lists/contaminant_type/dyes_and_pigments"])
    soft_trims_and_prints = PermissibleValue(
        text="soft_trims_and_prints",
        title="Soft trims and prints",
        meaning=T2T["lists/contaminant_type/soft_trims_and_prints"])
    hard_trims = PermissibleValue(
        text="hard_trims",
        title="Hard trims",
        meaning=T2T["lists/contaminant_type/hard_trims"])
    other_materials = PermissibleValue(
        text="other_materials",
        title="Other materials",
        meaning=T2T["lists/contaminant_type/other_materials"])

    _defn = EnumDefinition(
        name="ContaminantType",
    )

class ContaminantCoatingsAndFinishes(EnumDefinitionImpl):

    uv_resistant = PermissibleValue(
        text="uv_resistant",
        title="UV resistant",
        meaning=T2T["lists/contaminant_coatings_and_finishes/uv_resistant"])
    flame_retardant = PermissibleValue(
        text="flame_retardant",
        title="Flame retardant",
        meaning=T2T["lists/contaminant_coatings_and_finishes/flame_retardant"])
    fire_resistant = PermissibleValue(
        text="fire_resistant",
        title="Fire resistant",
        meaning=T2T["lists/contaminant_coatings_and_finishes/fire_resistant"])
    antimicrobial = PermissibleValue(
        text="antimicrobial",
        title="Antimicrobial",
        meaning=T2T["lists/contaminant_coatings_and_finishes/antimicrobial"])
    insect_repellent = PermissibleValue(
        text="insect_repellent",
        title="Insect repellent",
        meaning=T2T["lists/contaminant_coatings_and_finishes/insect_repellent"])
    non_slip_dimensional_stability = PermissibleValue(
        text="non_slip_dimensional_stability",
        title="Non-slip/dimensional stability",
        meaning=T2T["lists/contaminant_coatings_and_finishes/non_slip_dimensional_stability"])
    antistatic = PermissibleValue(
        text="antistatic",
        title="Antistatic",
        meaning=T2T["lists/contaminant_coatings_and_finishes/antistatic"])
    water_repellent = PermissibleValue(
        text="water_repellent",
        title="Water repellent",
        meaning=T2T["lists/contaminant_coatings_and_finishes/water_repellent"])
    dirt_repellent = PermissibleValue(
        text="dirt_repellent",
        title="Dirt repellent",
        meaning=T2T["lists/contaminant_coatings_and_finishes/dirt_repellent"])
    silicone = PermissibleValue(
        text="silicone",
        title="Silicone",
        meaning=T2T["lists/contaminant_coatings_and_finishes/silicone"])
    elastomeric = PermissibleValue(
        text="elastomeric",
        title="Elastomeric",
        meaning=T2T["lists/contaminant_coatings_and_finishes/elastomeric"])
    fabric_softening = PermissibleValue(
        text="fabric_softening",
        title="Fabric softening",
        meaning=T2T["lists/contaminant_coatings_and_finishes/fabric_softening"])
    fabric_stiffness = PermissibleValue(
        text="fabric_stiffness",
        title="Fabric stiffness",
        meaning=T2T["lists/contaminant_coatings_and_finishes/fabric_stiffness"])
    wrinkle_resistant = PermissibleValue(
        text="wrinkle_resistant",
        title="Wrinkle resistant",
        meaning=T2T["lists/contaminant_coatings_and_finishes/wrinkle_resistant"])
    fabric_hand = PermissibleValue(
        text="fabric_hand",
        title="Fabric hand",
        meaning=T2T["lists/contaminant_coatings_and_finishes/fabric_hand"])
    anti_pilling = PermissibleValue(
        text="anti_pilling",
        title="Anti-pilling",
        meaning=T2T["lists/contaminant_coatings_and_finishes/anti_pilling"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/contaminant_coatings_and_finishes/other"])

    _defn = EnumDefinition(
        name="ContaminantCoatingsAndFinishes",
    )

class ContaminantDyesAndPigments(EnumDefinitionImpl):

    natural_dyes = PermissibleValue(
        text="natural_dyes",
        title="Natural dyes",
        meaning=T2T["lists/contaminant_dyes_and_pigments/natural_dyes"])
    acid = PermissibleValue(
        text="acid",
        title="Acid",
        meaning=T2T["lists/contaminant_dyes_and_pigments/acid"])
    basic = PermissibleValue(
        text="basic",
        title="Basic",
        meaning=T2T["lists/contaminant_dyes_and_pigments/basic"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/contaminant_dyes_and_pigments/other"])

    _defn = EnumDefinition(
        name="ContaminantDyesAndPigments",
    )

class ContaminantSoftTrimsAndPrints(EnumDefinitionImpl):

    tape = PermissibleValue(
        text="tape",
        title="Tape",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/tape"])
    binding = PermissibleValue(
        text="binding",
        title="Binding",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/binding"])
    piping = PermissibleValue(
        text="piping",
        title="Piping",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/piping"])
    flag_label = PermissibleValue(
        text="flag_label",
        title="(Flag)label",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/flag_label"])
    interlining = PermissibleValue(
        text="interlining",
        title="Interlining",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/interlining"])
    sewing_thread = PermissibleValue(
        text="sewing_thread",
        title="Sewing thread",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/sewing_thread"])
    drawcord = PermissibleValue(
        text="drawcord",
        title="Drawcord",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/drawcord"])
    hook_and_loop_closure = PermissibleValue(
        text="hook_and_loop_closure",
        title="Hook & loop closure",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/hook_and_loop_closure"])
    heat_transfer = PermissibleValue(
        text="heat_transfer",
        title="Heat transfer",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/heat_transfer"])
    direct_screen_print = PermissibleValue(
        text="direct_screen_print",
        title="Direct screen print",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/direct_screen_print"])
    pigment_print = PermissibleValue(
        text="pigment_print",
        title="Pigment print",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/pigment_print"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/contaminant_soft_trims_and_prints/other"])

    _defn = EnumDefinition(
        name="ContaminantSoftTrimsAndPrints",
    )

class ContaminantHardTrims(EnumDefinitionImpl):

    button = PermissibleValue(
        text="button",
        title="Button",
        meaning=T2T["lists/contaminant_hard_trims/button"])
    snap_button = PermissibleValue(
        text="snap_button",
        title="Snap button",
        meaning=T2T["lists/contaminant_hard_trims/snap_button"])
    cord_stopper = PermissibleValue(
        text="cord_stopper",
        title="Cord stopper",
        meaning=T2T["lists/contaminant_hard_trims/cord_stopper"])
    aglet = PermissibleValue(
        text="aglet",
        title="Aglet",
        meaning=T2T["lists/contaminant_hard_trims/aglet"])
    metal_zip = PermissibleValue(
        text="metal_zip",
        title="Metal zip",
        meaning=T2T["lists/contaminant_hard_trims/metal_zip"])
    plastic_zip = PermissibleValue(
        text="plastic_zip",
        title="Plastic zip",
        meaning=T2T["lists/contaminant_hard_trims/plastic_zip"])
    puller = PermissibleValue(
        text="puller",
        title="Puller",
        meaning=T2T["lists/contaminant_hard_trims/puller"])
    hook_and_eye_closure = PermissibleValue(
        text="hook_and_eye_closure",
        title="Hook & eye closure",
        meaning=T2T["lists/contaminant_hard_trims/hook_and_eye_closure"])
    buckle = PermissibleValue(
        text="buckle",
        title="Buckle",
        meaning=T2T["lists/contaminant_hard_trims/buckle"])
    rivet = PermissibleValue(
        text="rivet",
        title="Rivet",
        meaning=T2T["lists/contaminant_hard_trims/rivet"])
    studs = PermissibleValue(
        text="studs",
        title="Studs",
        meaning=T2T["lists/contaminant_hard_trims/studs"])
    sequins = PermissibleValue(
        text="sequins",
        title="Sequins",
        meaning=T2T["lists/contaminant_hard_trims/sequins"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/contaminant_hard_trims/other"])

    _defn = EnumDefinition(
        name="ContaminantHardTrims",
    )

class ContaminantOtherMaterials(EnumDefinitionImpl):

    acrylic_polymer = PermissibleValue(
        text="acrylic_polymer",
        title="Acrylic (polymer)",
        meaning=T2T["lists/contaminant_other_materials/acrylic_polymer"])
    silicone = PermissibleValue(
        text="silicone",
        title="Silicone",
        meaning=T2T["lists/contaminant_other_materials/silicone"])
    polyacrylate = PermissibleValue(
        text="polyacrylate",
        title="Polyacrylate",
        meaning=T2T["lists/contaminant_other_materials/polyacrylate"])
    polyvinyl_chloride = PermissibleValue(
        text="polyvinyl_chloride",
        title="Polyvinyl chloride",
        meaning=T2T["lists/contaminant_other_materials/polyvinyl_chloride"])
    polytetrafluoroethylene = PermissibleValue(
        text="polytetrafluoroethylene",
        title="Polytetrafluoroethylene",
        meaning=T2T["lists/contaminant_other_materials/polytetrafluoroethylene"])
    polyoxymethylene = PermissibleValue(
        text="polyoxymethylene",
        title="Polyoxymethylene",
        meaning=T2T["lists/contaminant_other_materials/polyoxymethylene"])
    acrylonitrile_butadiene_styrene = PermissibleValue(
        text="acrylonitrile_butadiene_styrene",
        title="Acrylonitrile butadiene styrene",
        meaning=T2T["lists/contaminant_other_materials/acrylonitrile_butadiene_styrene"])
    aluminium = PermissibleValue(
        text="aluminium",
        title="Aluminium",
        meaning=T2T["lists/contaminant_other_materials/aluminium"])
    brass = PermissibleValue(
        text="brass",
        title="Brass",
        meaning=T2T["lists/contaminant_other_materials/brass"])
    zinc = PermissibleValue(
        text="zinc",
        title="Zinc",
        meaning=T2T["lists/contaminant_other_materials/zinc"])
    stainless_steel = PermissibleValue(
        text="stainless_steel",
        title="Stainless steel",
        meaning=T2T["lists/contaminant_other_materials/stainless_steel"])
    copper = PermissibleValue(
        text="copper",
        title="Copper",
        meaning=T2T["lists/contaminant_other_materials/copper"])
    ferrous_metal = PermissibleValue(
        text="ferrous_metal",
        title="Ferrous metal",
        meaning=T2T["lists/contaminant_other_materials/ferrous_metal"])
    non_ferrous_metal = PermissibleValue(
        text="non_ferrous_metal",
        title="Non-ferrous metal",
        meaning=T2T["lists/contaminant_other_materials/non_ferrous_metal"])
    polylactide = PermissibleValue(
        text="polylactide",
        title="Polylactide",
        meaning=T2T["lists/contaminant_other_materials/polylactide"])
    polyethylene_furanoate = PermissibleValue(
        text="polyethylene_furanoate",
        title="Polyethylene furanoate",
        meaning=T2T["lists/contaminant_other_materials/polyethylene_furanoate"])
    aramid = PermissibleValue(
        text="aramid",
        title="Aramid",
        meaning=T2T["lists/contaminant_other_materials/aramid"])
    carbon = PermissibleValue(
        text="carbon",
        title="Carbon",
        meaning=T2T["lists/contaminant_other_materials/carbon"])
    glass = PermissibleValue(
        text="glass",
        title="Glass",
        meaning=T2T["lists/contaminant_other_materials/glass"])
    pfas = PermissibleValue(
        text="pfas",
        title="PFAS",
        meaning=T2T["lists/contaminant_other_materials/pfas"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/contaminant_other_materials/other"])

    _defn = EnumDefinition(
        name="ContaminantOtherMaterials",
    )

class ContaminantAmountUnit(EnumDefinitionImpl):

    percent_of_total_batch_weight = PermissibleValue(
        text="percent_of_total_batch_weight",
        title="% of total batch weight",
        meaning=T2T["lists/contaminant_amount_unit/percent_of_total_batch_weight"])
    percent_of_total_fiber_composition = PermissibleValue(
        text="percent_of_total_fiber_composition",
        title="% of total fiber composition",
        meaning=T2T["lists/contaminant_amount_unit/percent_of_total_fiber_composition"])
    ppm = PermissibleValue(
        text="ppm",
        title="PPM",
        meaning=T2T["lists/contaminant_amount_unit/ppm"])

    _defn = EnumDefinition(
        name="ContaminantAmountUnit",
    )

class ContaminantThreshold(EnumDefinitionImpl):

    measured_value = PermissibleValue(
        text="measured_value",
        title="Measured value",
        meaning=T2T["lists/contaminant_threshold/measured_value"])
    maximum = PermissibleValue(
        text="maximum",
        title="Maximum",
        meaning=T2T["lists/contaminant_threshold/maximum"])
    trace_amounts_accepted = PermissibleValue(
        text="trace_amounts_accepted",
        title="Trace amounts accepted",
        meaning=T2T["lists/contaminant_threshold/trace_amounts_accepted"])
    zero_tolerance = PermissibleValue(
        text="zero_tolerance",
        title="Zero tolerance",
        meaning=T2T["lists/contaminant_threshold/zero_tolerance"])

    _defn = EnumDefinition(
        name="ContaminantThreshold",
    )

class ContaminantCheck(EnumDefinitionImpl):

    not_evaluated = PermissibleValue(
        text="not_evaluated",
        title="Not evaluated",
        meaning=T2T["lists/contaminant_check/not_evaluated"])
    detected = PermissibleValue(
        text="detected",
        title="Detected",
        meaning=T2T["lists/contaminant_check/detected"])
    not_detected = PermissibleValue(
        text="not_detected",
        title="Not detected",
        meaning=T2T["lists/contaminant_check/not_detected"])

    _defn = EnumDefinition(
        name="ContaminantCheck",
    )

class Format(EnumDefinitionImpl):

    clippings = PermissibleValue(
        text="clippings",
        title="Clippings",
        description="Produced by chopping or cutting textiles into smaller pieces during feedstock preparation",
        meaning=T2T["lists/format/clippings"])
    cutting_waste = PermissibleValue(
        text="cutting_waste",
        title="Cutting waste",
        description="Produced by manufacturers when cutting markers",
        meaning=T2T["lists/format/cutting_waste"])
    dust_powder = PermissibleValue(
        text="dust_powder",
        title="Dust/powder",
        meaning=T2T["lists/format/dust_powder"])
    fiber = PermissibleValue(
        text="fiber",
        title="Fiber",
        meaning=T2T["lists/format/fiber"])
    flakes = PermissibleValue(
        text="flakes",
        title="Flakes",
        meaning=T2T["lists/format/flakes"])
    garments_linens_household_textiles = PermissibleValue(
        text="garments_linens_household_textiles",
        title="Garments / linens / household textiles",
        meaning=T2T["lists/format/garments_linens_household_textiles"])
    granules = PermissibleValue(
        text="granules",
        title="Granules",
        meaning=T2T["lists/format/granules"])
    monomers = PermissibleValue(
        text="monomers",
        title="Monomers",
        meaning=T2T["lists/format/monomers"])
    opened_fiber = PermissibleValue(
        text="opened_fiber",
        title="Opened fiber",
        description="""Textile that has been shredded or torn into fiber or a mix of fiber and pieces of textiles during feedstock preparation""",
        meaning=T2T["lists/format/opened_fiber"])
    pellets = PermissibleValue(
        text="pellets",
        title="Pellets",
        meaning=T2T["lists/format/pellets"])
    polymers = PermissibleValue(
        text="polymers",
        title="Polymers",
        meaning=T2T["lists/format/polymers"])
    pulp = PermissibleValue(
        text="pulp",
        title="Pulp",
        meaning=T2T["lists/format/pulp"])
    sliver = PermissibleValue(
        text="sliver",
        title="Sliver",
        meaning=T2T["lists/format/sliver"])
    trim = PermissibleValue(
        text="trim",
        title="Trim",
        meaning=T2T["lists/format/trim"])
    yarn = PermissibleValue(
        text="yarn",
        title="Yarn",
        meaning=T2T["lists/format/yarn"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/format/other"])

    _defn = EnumDefinition(
        name="Format",
    )

class PhysicalPropertyName(EnumDefinitionImpl):

    brightness = PermissibleValue(
        text="brightness",
        title="Brightness",
        meaning=T2T["lists/physical_property_name/brightness"])
    crystallinity = PermissibleValue(
        text="crystallinity",
        title="Crystallinity",
        meaning=T2T["lists/physical_property_name/crystallinity"])
    degree_of_polymerization_dp = PermissibleValue(
        text="degree_of_polymerization_dp",
        title="Degree of Polymerization (DP)",
        meaning=T2T["lists/physical_property_name/degree_of_polymerization_dp"])
    density = PermissibleValue(
        text="density",
        title="Density",
        meaning=T2T["lists/physical_property_name/density"])
    fiber_length = PermissibleValue(
        text="fiber_length",
        title="Fiber Length",
        meaning=T2T["lists/physical_property_name/fiber_length"])
    intrinsic_viscosity_iv = PermissibleValue(
        text="intrinsic_viscosity_iv",
        title="Intrinsic Viscosity (IV)",
        meaning=T2T["lists/physical_property_name/intrinsic_viscosity_iv"])
    moisture_dry_matter_content = PermissibleValue(
        text="moisture_dry_matter_content",
        title="Moisture/Dry Matter Content",
        meaning=T2T["lists/physical_property_name/moisture_dry_matter_content"])
    molecular_weight_mw_mn = PermissibleValue(
        text="molecular_weight_mw_mn",
        title="Molecular Weight (Mw/Mn)",
        meaning=T2T["lists/physical_property_name/molecular_weight_mw_mn"])
    piece_size = PermissibleValue(
        text="piece_size",
        title="Piece size",
        meaning=T2T["lists/physical_property_name/piece_size"])
    rheology = PermissibleValue(
        text="rheology",
        title="Rheology",
        meaning=T2T["lists/physical_property_name/rheology"])
    thermal_properties_tm_tg = PermissibleValue(
        text="thermal_properties_tm_tg",
        title="Thermal Properties (Tm, Tg)",
        meaning=T2T["lists/physical_property_name/thermal_properties_tm_tg"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=T2T["lists/physical_property_name/other"])

    _defn = EnumDefinition(
        name="PhysicalPropertyName",
    )

class PhysicalPropertyUnit(EnumDefinitionImpl):

    cm = PermissibleValue(
        text="cm",
        title="cm",
        meaning=T2T["lists/physical_property_unit/cm"])
    delta_e = PermissibleValue(
        text="delta_e",
        title="∆E",
        meaning=T2T["lists/physical_property_unit/delta_e"])
    ml_per_g = PermissibleValue(
        text="ml_per_g",
        title="mL/g",
        meaning=T2T["lists/physical_property_unit/ml_per_g"])
    dl_per_g = PermissibleValue(
        text="dl_per_g",
        title="dL/g",
        meaning=T2T["lists/physical_property_unit/dl_per_g"])
    g_per_cm3 = PermissibleValue(
        text="g_per_cm3",
        title="g/cm^3",
        meaning=T2T["lists/physical_property_unit/g_per_cm3"])
    percent = PermissibleValue(
        text="percent",
        title="%",
        meaning=T2T["lists/physical_property_unit/percent"])

    _defn = EnumDefinition(
        name="PhysicalPropertyUnit",
    )

class FabricConstruction(EnumDefinitionImpl):

    knit = PermissibleValue(
        text="knit",
        title="Knit",
        meaning=T2T["lists/fabric_construction/knit"])
    woven = PermissibleValue(
        text="woven",
        title="Woven",
        meaning=T2T["lists/fabric_construction/woven"])
    non_woven = PermissibleValue(
        text="non_woven",
        title="Non-woven",
        meaning=T2T["lists/fabric_construction/non_woven"])
    mixed_construction = PermissibleValue(
        text="mixed_construction",
        title="Mixed construction",
        meaning=T2T["lists/fabric_construction/mixed_construction"])

    _defn = EnumDefinition(
        name="FabricConstruction",
    )

class YesNo(EnumDefinitionImpl):

    yes = PermissibleValue(
        text="yes",
        title="Yes",
        meaning=T2T["lists/yes_no/yes"])
    no = PermissibleValue(
        text="no",
        title="No",
        meaning=T2T["lists/yes_no/no"])

    _defn = EnumDefinition(
        name="YesNo",
    )

# Slots
class slots:
    pass

slots.material_sources = Slot(uri=T2T.material_sources, name="material_sources", curie=T2T.curie('material_sources'),
                   model_uri=T2T.material_sources, domain=None, range=Optional[Union[Union[str, "MaterialSource"], list[Union[str, "MaterialSource"]]]])

slots.internal_product_name = Slot(uri=T2T.internal_product_name, name="internal_product_name", curie=T2T.curie('internal_product_name'),
                   model_uri=T2T.internal_product_name, domain=None, range=Optional[str])

slots.color_generic = Slot(uri=T2T.color_generic, name="color_generic", curie=T2T.curie('color_generic'),
                   model_uri=T2T.color_generic, domain=None, range=Optional[Union[str, "ColorGeneric"]])

slots.fiber_composition_name = Slot(uri=T2T.fiber_composition_name, name="fiber_composition_name", curie=T2T.curie('fiber_composition_name'),
                   model_uri=T2T.fiber_composition_name, domain=None, range=Optional[Union[str, "FiberCompositionName"]])

slots.fiber_composition_value = Slot(uri=T2T.fiber_composition_value, name="fiber_composition_value", curie=T2T.curie('fiber_composition_value'),
                   model_uri=T2T.fiber_composition_value, domain=None, range=Optional[Decimal])

slots.fiber_composition_threshold = Slot(uri=T2T.fiber_composition_threshold, name="fiber_composition_threshold", curie=T2T.curie('fiber_composition_threshold'),
                   model_uri=T2T.fiber_composition_threshold, domain=None, range=Optional[Union[str, "FiberCompositionThreshold"]])

slots.contaminant_type = Slot(uri=T2T.contaminant_type, name="contaminant_type", curie=T2T.curie('contaminant_type'),
                   model_uri=T2T.contaminant_type, domain=None, range=Optional[Union[str, "ContaminantType"]])

slots.contaminant_name = Slot(uri=T2T.contaminant_name, name="contaminant_name", curie=T2T.curie('contaminant_name'),
                   model_uri=T2T.contaminant_name, domain=None, range=Optional[Union[str, "FiberCompositionName", "ContaminantCoatingsAndFinishes", "ContaminantDyesAndPigments", "ContaminantSoftTrimsAndPrints", "ContaminantHardTrims", "ContaminantOtherMaterials"]])

slots.contaminant_amount = Slot(uri=T2T.contaminant_amount, name="contaminant_amount", curie=T2T.curie('contaminant_amount'),
                   model_uri=T2T.contaminant_amount, domain=None, range=Optional[Decimal])

slots.contaminant_amount_unit = Slot(uri=T2T.contaminant_amount_unit, name="contaminant_amount_unit", curie=T2T.curie('contaminant_amount_unit'),
                   model_uri=T2T.contaminant_amount_unit, domain=None, range=Optional[Union[str, "ContaminantAmountUnit"]])

slots.contaminant_threshold = Slot(uri=T2T.contaminant_threshold, name="contaminant_threshold", curie=T2T.curie('contaminant_threshold'),
                   model_uri=T2T.contaminant_threshold, domain=None, range=Optional[Union[str, "ContaminantThreshold"]])

slots.contaminant_check = Slot(uri=T2T.contaminant_check, name="contaminant_check", curie=T2T.curie('contaminant_check'),
                   model_uri=T2T.contaminant_check, domain=None, range=Optional[Union[str, "ContaminantCheck"]])

slots.contaminant_hazardous_substance = Slot(uri=T2T.contaminant_hazardous_substance, name="contaminant_hazardous_substance", curie=T2T.curie('contaminant_hazardous_substance'),
                   model_uri=T2T.contaminant_hazardous_substance, domain=None, range=Optional[Union[str, "YesNo"]])

slots.contaminant_sds = Slot(uri=T2T.contaminant_sds, name="contaminant_sds", curie=T2T.curie('contaminant_sds'),
                   model_uri=T2T.contaminant_sds, domain=None, range=Optional[Union[str, URI]])

slots.contaminant_explanation = Slot(uri=T2T.contaminant_explanation, name="contaminant_explanation", curie=T2T.curie('contaminant_explanation'),
                   model_uri=T2T.contaminant_explanation, domain=None, range=Optional[str])

slots.contaminant_evidence = Slot(uri=T2T.contaminant_evidence, name="contaminant_evidence", curie=T2T.curie('contaminant_evidence'),
                   model_uri=T2T.contaminant_evidence, domain=None, range=Optional[Union[str, URI]])

slots.format = Slot(uri=T2T.format, name="format", curie=T2T.curie('format'),
                   model_uri=T2T.format, domain=None, range=Optional[Union[str, "Format"]])

slots.physical_property_name = Slot(uri=T2T.physical_property_name, name="physical_property_name", curie=T2T.curie('physical_property_name'),
                   model_uri=T2T.physical_property_name, domain=None, range=Optional[Union[str, "PhysicalPropertyName"]])

slots.physical_property_value = Slot(uri=T2T.physical_property_value, name="physical_property_value", curie=T2T.curie('physical_property_value'),
                   model_uri=T2T.physical_property_value, domain=None, range=Optional[Decimal])

slots.physical_property_unit = Slot(uri=T2T.physical_property_unit, name="physical_property_unit", curie=T2T.curie('physical_property_unit'),
                   model_uri=T2T.physical_property_unit, domain=None, range=Optional[Union[str, "PhysicalPropertyUnit"]])

slots.physical_property_verification_method = Slot(uri=T2T.physical_property_verification_method, name="physical_property_verification_method", curie=T2T.curie('physical_property_verification_method'),
                   model_uri=T2T.physical_property_verification_method, domain=None, range=Optional[str])

slots.fabric_construction = Slot(uri=T2T.fabric_construction, name="fabric_construction", curie=T2T.curie('fabric_construction'),
                   model_uri=T2T.fabric_construction, domain=None, range=Optional[Union[str, "FabricConstruction"]])

slots.recycled_content_in_outputs = Slot(uri=T2T.recycled_content_in_outputs, name="recycled_content_in_outputs", curie=T2T.curie('recycled_content_in_outputs'),
                   model_uri=T2T.recycled_content_in_outputs, domain=None, range=Optional[Union[str, "YesNo"]])

slots.recycled_content_source = Slot(uri=T2T.recycled_content_source, name="recycled_content_source", curie=T2T.curie('recycled_content_source'),
                   model_uri=T2T.recycled_content_source, domain=None, range=Optional[Union[str, "MaterialSource"]])

slots.recycled_content_value = Slot(uri=T2T.recycled_content_value, name="recycled_content_value", curie=T2T.curie('recycled_content_value'),
                   model_uri=T2T.recycled_content_value, domain=None, range=Optional[Decimal])

slots.certificate_of_analysis = Slot(uri=T2T.certificate_of_analysis, name="certificate_of_analysis", curie=T2T.curie('certificate_of_analysis'),
                   model_uri=T2T.certificate_of_analysis, domain=None, range=Optional[Union[str, URI]])

slots.fiber_compositions = Slot(uri=T2T.fiber_compositions, name="fiber_compositions", curie=T2T.curie('fiber_compositions'),
                   model_uri=T2T.fiber_compositions, domain=None, range=Optional[Union[Union[dict, FiberComposition], list[Union[dict, FiberComposition]]]])

slots.contaminants = Slot(uri=T2T.contaminants, name="contaminants", curie=T2T.curie('contaminants'),
                   model_uri=T2T.contaminants, domain=None, range=Optional[Union[Union[dict, Contaminant], list[Union[dict, Contaminant]]]])

slots.physical_properties = Slot(uri=T2T.physical_properties, name="physical_properties", curie=T2T.curie('physical_properties'),
                   model_uri=T2T.physical_properties, domain=None, range=Optional[Union[Union[dict, PhysicalProperty], list[Union[dict, PhysicalProperty]]]])

slots.recycled_contents = Slot(uri=T2T.recycled_contents, name="recycled_contents", curie=T2T.curie('recycled_contents'),
                   model_uri=T2T.recycled_contents, domain=None, range=Optional[Union[Union[dict, RecycledContent], list[Union[dict, RecycledContent]]]])
