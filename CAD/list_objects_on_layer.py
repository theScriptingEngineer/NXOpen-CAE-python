import NXOpen
from typing import List, cast


the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def list_objects_on_layer(layer: int):
    if not the_lw.IsOpen:
        the_lw.Open()
    layer_manager: NXOpen.Layer.LayerManager = base_part.Layers
    objects_on_layer: List[NXOpen.NXObject] = layer_manager.GetAllObjectsOnLayer(layer)
    the_lw.WriteFullline("")
    the_lw.WriteFullline("There are " + str(len(objects_on_layer)) + " objects on layer " + str(layer) + ":")
    for item in objects_on_layer:
        the_lw.WriteFullline("\t" + item.JournalIdentifier + " " + str(type(item)))


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    list_objects_on_layer(62)


if __name__ == '__main__':
    main()