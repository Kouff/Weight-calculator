def calculate_weight(data: list) -> dict:
    def get_weight(id: int, elem: dict, checked_elems: list = []) -> int:
        checked_elems = checked_elems.copy()  # copy the list
        if id in checked_elems:  # if the child`s weight is already in parent`s weight, return 0
            return 0
        else:  # else add to the list
            checked_elems.append(id)
        weight: int = elem['weight']  # get element`s weight
        child_elems: int = elem['elems']  # get all the child elements of parent element
        for child_elem in child_elems:
            # add all the weight of child elements to parent element`s weight
            weight += get_weight(child_elem, data[child_elem], checked_elems)
        return weight  # return all the parent element`s weight

    # make a dict with id elements as keys
    # [{'id': 1, 'weight': 1, 'elems': [1]}] -> {1: {'weight': 1, 'elems': [1]}}
    data = {obj.pop('id'): obj for obj in data}
    weights = {}
    for key, value in data.items():
        weights[key] = get_weight(key, value)
    return weights
