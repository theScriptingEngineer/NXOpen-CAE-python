import NXOpen
from typing import List, cast


the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def indentation(level: int) -> str:
    """Helper method to create indentations (eg tabs) with a given length.
       Can be used in print strings in a tree like structure

    Parameters
    ----------
    level: int
        The depth of the indentations.

    Returns
    -------
    str
        The indentation
    """
    indentation: str = ""
    for i in range(level + 1):
        indentation += "\t"
    
    return indentation


def print_history_tree(my_feature: NXOpen.Features.Feature, requested_level: int = 0) -> None:
    """Prints the component tree for the given component to the listing window.
       Recursive function

    Parameters
    ----------
    component: NXOpen.Assemblies.Component
        The component for whch to print the component tree
    requested_level: int
        Optional parameter used for creating indentations.
    """
    level: int = requested_level
    the_lw.WriteFullline(indentation(level) + "| " + my_feature.JournalIdentifier + " with name " + my_feature.GetFeatureName())
    children: List[NXOpen.Features.Feature] = my_feature.GetChildren()
    for i in range(len(children)):
        print_history_tree(children[i], level + 1)


def get_all_features(part: NXOpen.Part = None) -> List[NXOpen.Features.Feature]:
    """Gets all features in the base_part

    Parameters
    ----------
    part: NXOpen.Part (optional)
        The part to return the features for. Takes the base_part if not given.
    
    Returns
    -------
    List[NXOpen.Features.Feature]
        A list with all features.
    """
    all_features: List[NXOpen.Features.Feature] = []
    part_for_features: NXOpen.Part = cast(NXOpen.Part, base_part)
    if part != None:
        part_for_features = part
    for item in part_for_features.Features:
        all_features.append(item)
    return all_features


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    all_features: List[NXOpen.Features.Feature] = get_all_features()
    # the first feature is the basic datum coordinate system. All the rest depends on this.
    print_history_tree(all_features[0])


if __name__ == '__main__':
    main()
