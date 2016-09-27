import TextPreprocessors
import TokenSupervised
import ContextVectorGenerators

# A supervised classification module that can be used for detecting wrong/right annotations

def data_preparation_script_1(jlines_file, embeddings_file, text_attribute, annotated_attribute,
                              correct_attribute, output_folder):
    """
    At present, this script cannot deal with multi-token annotations (e.g. 'Mary Ann' or 'Salt lake city'). We
    will convert all tokens to lower-case; thus, case-differences will not be accounted for.

    Two files will be written out to the output_folder, one of which will be intermediate, and the other of which
    is the file on which we will train/test the machine learning model.
    :param jlines_file: A file where each line is a json.
    :param embeddings_file: At present, use the provided file; do not try to generate it yourself
    :param text_attribute: e.g. 'high_recall_readability_text'
    :param annotated_attribute: e.g. 'annotated_cities'
    :param correct_attribute: e.g. 'correct_cities'
    :param output_folder: a folder for writing out files in
    :return: None
    """
    TextPreprocessors.TextPreprocessors.preprocess_annotated_file(jlines_file, text_attribute,
                                                                  output_folder+'tokens-file.jl')
    TokenSupervised.TokenSupervised.prep_preprocessed_annotated_file_for_classification(output_folder+'tokens-file.jl',
                embeddings_file, output_folder+'pos-neg-file.txt',
                ContextVectorGenerators.ContextVectorGenerators.symmetric_generator,
                text_attribute, annotated_attribute, correct_attribute)


def classification_script_1(pos_neg_file):
    """
    Run this code after running a data preparation script.
    Prints out a bunch of metrics.
    :param pos_neg_file: This is the pos-neg-file.txt generated by data preparation in the output folder.
    :return: None
    """
    TokenSupervised.TokenSupervised.trial_script_binary(pos_neg_file)


# path = '/Users/mayankkejriwal/ubuntu-vm-stuff/home/mayankkejriwal/tmp/annotated-cities-trial/'
# path = '/Users/mayankkejriwal/ubuntu-vm-stuff/home/mayankkejriwal/Downloads/memex-cp4-october/supervised-exp-datasets/'
# data_preparation_script_1(path+'annotated-cities-2.json', path+'unigram-part-00000-v2.json',
#                           'high_recall_readability_text', 'annotated_cities', 'correct_cities', path+'output_folder/')
# classification_script_1(path+'output_folder/pos-neg-file.txt')