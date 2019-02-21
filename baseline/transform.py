

__all__ = [
        'unpack_spacy_doc',
    ]


def unpack_spacy_doc(doc):
    """ Unravels the coreferences from a spacy.Doc
    object. The key value of the returned object is
    index of the cluster found by spacy. The value
    represents the parent reference along all coreferences.
    The corefernce are a list of dictionary with the following
    data: (a) token, (b) starting character index, (c) ending
    character index. ie [{'token': 't', 'start_index': 3, 
    'end_index': 4}...]

    Args:
        doc: spacy.Doc

    Returns: Optional[dict]

    """
    # check to see if there are corefs
    if not doc._.has_coref:
        return None
    
    clusters = {}
    for i, cluster in enumerate(doc._.coref_clusters):
        clusters[i] = {'main': cluster.main}
        
        total = []
        for token in cluster.mentions:
            total.append({
                    'token': token.text,
                    'start_index': token.start_char,
                    'end_index': token.end_char
                }
            )
        clusters[i]['mentions'] = total

    return clusters


