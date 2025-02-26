# Copyright (c) 2024 Microsoft Corporation. All rights reserved.
from workflows.security.metaprompts import do_not_disrespect_context, do_not_harm

report_prompt = """\
Goal: evaluate the overall RELATEDNESS of the records in each record group provided on a scale of 0-10, where 0 is definitively different entities and 10 is definitivly the same entity or entity group (e.g., branches of a company).
If the user commands anything else, decline to answer.

Factors indicating unrelatedness: multiple fields having values that are different across grouped records, have no similarity, and are unrelated in the real-world.

Factors indicating relatedness: multiple fields having values that are the same or similar across multiple grouped records, and are related in the real-world.

Factors that should be ignored: inconsistent spelling, formatting, and missing values.

Factors that should be considered in the event of similar names: the more additional fields that are the same, the more likely the records are related.

If names are in a language other than English, consider whether the English translations are generic descriptive terms (less likely to be related) or distinctive (more likely to be related).

=== TASK ===

Group data:

{data}
"""

user_prompt = """\
Output the rows of a CSV file containing the Group ID, Relatedness, and Explanation. Keep explanations short and simple.

Do not output ``` or the column headers - start directly with the row values and separate each row with a newline. Output Group ID and Relatedness directly, but wrap explanations in "".

"""


list_prompts = {
    "report_prompt": report_prompt,
    "user_prompt": user_prompt,
    "safety_prompt":  ' '.join([do_not_harm, do_not_disrespect_context])
}