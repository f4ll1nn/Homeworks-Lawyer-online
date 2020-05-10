from samles import Samples

file_name = "2.csv"
book = Samples(file_name)
book.situation_sample_read()
df_stat = book.choising_relevant_rows(param="df")
indexes = book.choising_relevant_rows(param="index")
df_old = book.choising_relevant_rows(param="df_old")
df_new = book.creating_df_for_result(df_stat)
list_punkts = book.choising_sentences(indexes, df_old)
df_new = book.creating_samples_df(df_new, list_punkts)
book.save_samples()