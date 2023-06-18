# imports

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# sparql wrapper
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")


# Util functions for Migraine: Q133823

# Histogram: symptoms count
def plot_symptoms_count_histogram():
    query_migraine = '''
    PREFIX target: <http://www.wikidata.org/entity/Q133823>

    SELECT
      ?count
      ?gene_count
      ?symptom_count
      ?disease ?diseaseLabel
      ?genes
      ?symptoms
    {
      {
        SELECT ?disease (COUNT(?gene) AS ?gene_count) (GROUP_CONCAT(?gene_label; separator=" // ") AS ?genes) WHERE {
          target: wdt:P2293 ?gene .
          ?gene wdt:P2293 ?disease .
          FILTER (target: != ?disease)
          ?gene rdfs:label ?gene_label
          FILTER(lang(?gene_label) = "en")
        }
        GROUP BY ?disease
      }
      UNION
      {
        SELECT
          ?disease (COUNT(?symptom) AS ?symptom_count) (GROUP_CONCAT(?symptom_label; separator=" // ") AS ?symptoms)
        {
          target: wdt:P780 ?symptom .
          ?disease wdt:P780 ?symptom .
          FILTER (target: != ?disease)
          ?symptom rdfs:label ?symptom_label . FILTER(lang(?symptom_label) = "en")
        }
        GROUP BY ?disease
      }

      # Aggregate count
      BIND((COALESCE(?symptom_count, 0) + COALESCE(?gene_count, 0)) AS ?count)

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?count)
    '''

    sparql.setQuery(query_migraine)
    sparql.setReturnFormat(JSON)
    results_migraine = sparql.query().convert()

    reformatted_dict_migraine = {}

    entities_migraine = []
    result_list_migraine = results_migraine['results']['bindings']
    for res in result_list_migraine:
        for res_key, res_value in res.items():
            if res_key == 'disease':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                entities_migraine.append(entity_id)
                reformatted_dict_migraine[entity_id] = res

    df_migraine = pd.DataFrame.from_dict(reformatted_dict_migraine)
    df_migraine = df_migraine.transpose()

    df_migraine = df_migraine.apply(lambda x: x.apply(lambda y: y['value'] if type(y) == dict else y))

    for index, row in df_migraine.iterrows():
        if isinstance(row['symptoms'], str):
            row['symptoms'] = row['symptoms'].split(' // ')

    df_migraine_explode = df_migraine.explode('symptoms')
    series = df_migraine_explode.symptoms.value_counts()
    symptoms_count = pd.DataFrame(series)

    # plot
    fig = px.histogram(symptoms_count, y=symptoms_count["count"], x=symptoms_count.index)
    fig.update_layout(
        title="Migraine related diseases symptoms",
        xaxis_title="Symptoms per related disease",
        yaxis_title="Number of diseases with symptom",
        width=500)
    return fig


# Pie plot: symptoms count
def pie_plot_symptoms():
    query_migraine = '''
    PREFIX target: <http://www.wikidata.org/entity/Q133823>

    SELECT
      ?count
      ?gene_count
      ?symptom_count
      ?disease ?diseaseLabel
      ?genes
      ?symptoms
    {
      {
        SELECT ?disease (COUNT(?gene) AS ?gene_count) (GROUP_CONCAT(?gene_label; separator=" // ") AS ?genes) WHERE {
          target: wdt:P2293 ?gene .
          ?gene wdt:P2293 ?disease .
          FILTER (target: != ?disease)
          ?gene rdfs:label ?gene_label
          FILTER(lang(?gene_label) = "en")
        }
        GROUP BY ?disease
      }
      UNION
      {
        SELECT
          ?disease (COUNT(?symptom) AS ?symptom_count) (GROUP_CONCAT(?symptom_label; separator=" // ") AS ?symptoms)
        {
          target: wdt:P780 ?symptom .
          ?disease wdt:P780 ?symptom .
          FILTER (target: != ?disease)
          ?symptom rdfs:label ?symptom_label . FILTER(lang(?symptom_label) = "en")
        }
        GROUP BY ?disease
      }

      # Aggregate count
      BIND((COALESCE(?symptom_count, 0) + COALESCE(?gene_count, 0)) AS ?count)

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?count)
    '''

    sparql.setQuery(query_migraine)
    sparql.setReturnFormat(JSON)
    results_migraine = sparql.query().convert()

    reformatted_dict_migraine = {}

    entities_migraine = []
    result_list_migraine = results_migraine['results']['bindings']
    for res in result_list_migraine:
        for res_key, res_value in res.items():
            if res_key == 'disease':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                entities_migraine.append(entity_id)
                reformatted_dict_migraine[entity_id] = res

    df_migraine = pd.DataFrame.from_dict(reformatted_dict_migraine)
    df_migraine = df_migraine.transpose()

    df_migraine = df_migraine.apply(lambda x: x.apply(lambda y: y['value'] if type(y) == dict else y))

    for index, row in df_migraine.iterrows():
        if isinstance(row['symptoms'], str):
            row['symptoms'] = row['symptoms'].split(' // ')

    df_migraine_explode = df_migraine.explode('symptoms')
    series = df_migraine_explode.symptoms.value_counts()
    symptoms_count = pd.DataFrame({'symptoms': series.index, 'count': series.values})

    # plot
    fig = go.Figure(data=[go.Pie(labels=symptoms_count.index,
                                 values=symptoms_count["count"],
                                 hole=.3)])
    fig.update_layout(title_text='Percentage share of symptoms for Migraine and related diseases')
    return fig


# Histogram: Treatments
def plot_histogram():
    query_migraine = '''
    PREFIX target: <http://www.wikidata.org/entity/Q133823>

    SELECT
      ?count
      ?treatment_count
      ?disease ?diseaseLabel
      ?treatments
    {
      {
        SELECT ?disease (COUNT(?treatment) AS ?treatment_count) (GROUP_CONCAT(?treatment_label; separator=" // ") AS ?treatments) WHERE {
          target: wdt:P2176 ?treatment .
          ?disease wdt:P2176 ?treatment .
          FILTER (target: != ?disease)
          ?treatment rdfs:label ?treatment_label
          FILTER(lang(?treatment_label) = "en")
        }
        GROUP BY ?disease
      }

      # Aggregate count
      BIND((COALESCE(?treatment_count, 0)) AS ?count)

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?count)
    '''

    sparql.setQuery(query_migraine)
    sparql.setReturnFormat(JSON)
    results_migraine = sparql.query().convert()

    reformatted_dict_migraine = {}

    entities_migraine = []
    result_list_migraine = results_migraine['results']['bindings']
    for res in result_list_migraine:
        for res_key, res_value in res.items():
            if res_key == 'disease':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                entities_migraine.append(entity_id)
                reformatted_dict_migraine[entity_id] = res

    df_migraine2 = pd.DataFrame.from_dict(reformatted_dict_migraine)
    df_migraine2 = df_migraine2.transpose()
    df_migraine2 = df_migraine2.apply(lambda x: x.apply(lambda y: y['value'] if type(y) == dict else y))

    for index, row in df_migraine2.iterrows():
        row['treatments'] = row['treatments'].split(' // ')

    df_migraine_explode2 = df_migraine2.explode('treatments')
    series2 = df_migraine_explode2.treatments.value_counts()
    drugs_count = pd.DataFrame({'treatments': series2.index, 'count': series2.values})

    # plot
    fig = px.histogram(drugs_count, y=drugs_count["count"], x=drugs_count.index)
    return fig


# Pie plot: Percentage share of treatments for Migraine and related diseases
def pie_plot():
    query_migraine = '''
    PREFIX target: <http://www.wikidata.org/entity/Q133823>

    SELECT
      ?count
      ?treatment_count
      ?disease ?diseaseLabel
      ?treatments
    {
      {
        SELECT ?disease (COUNT(?treatment) AS ?treatment_count) (GROUP_CONCAT(?treatment_label; separator=" // ") AS ?treatments) WHERE {
          target: wdt:P2176 ?treatment .
          ?disease wdt:P2176 ?treatment .
          FILTER (target: != ?disease)
          ?treatment rdfs:label ?treatment_label
          FILTER(lang(?treatment_label) = "en")
        }
        GROUP BY ?disease
      }

      # Aggregate count
      BIND((COALESCE(?treatment_count, 0)) AS ?count)

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?count)
    '''

    sparql.setQuery(query_migraine)
    sparql.setReturnFormat(JSON)
    results_migraine = sparql.query().convert()

    reformatted_dict_migraine = {}

    entities_migraine = []
    result_list_migraine = results_migraine['results']['bindings']
    for res in result_list_migraine:
        for res_key, res_value in res.items():
            if res_key == 'disease':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                entities_migraine.append(entity_id)
                reformatted_dict_migraine[entity_id] = res

    df_migraine2 = pd.DataFrame.from_dict(reformatted_dict_migraine)
    df_migraine2 = df_migraine2.transpose()
    df_migraine2 = df_migraine2.apply(lambda x: x.apply(lambda y: y['value'] if type(y) == dict else y))

    for index, row in df_migraine2.iterrows():
        row['treatments'] = row['treatments'].split(' // ')

    df_migraine_explode2 = df_migraine2.explode('treatments')

    # Get the counts of the treatments
    treatment_counts = df_migraine_explode2['treatments'].value_counts()

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=treatment_counts.index,
                                 values=treatment_counts.values,
                                 hole=.3)])  # Creating a "donut" style pie chart

    # Add title to the plot
    fig.update_layout(title_text='Percentage share of treatments for Migraine and related diseases')

    return fig


# Histogram: Number of diseases with x amount of symptoms
def plot_symptoms_histogram():
    query_migraine = '''
    PREFIX target: <http://www.wikidata.org/entity/Q133823>

    SELECT
      ?count
      ?gene_count
      ?symptom_count
      ?disease ?diseaseLabel
      ?genes
      ?symptoms
    {
      {
        SELECT ?disease (COUNT(?gene) AS ?gene_count) (GROUP_CONCAT(?gene_label; separator=" // ") AS ?genes) WHERE {
          target: wdt:P2293 ?gene .
          ?gene wdt:P2293 ?disease .
          FILTER (target: != ?disease)
          ?gene rdfs:label ?gene_label
          FILTER(lang(?gene_label) = "en")
        }
        GROUP BY ?disease
      }
      UNION
      {
        SELECT
          ?disease (COUNT(?symptom) AS ?symptom_count) (GROUP_CONCAT(?symptom_label; separator=" // ") AS ?symptoms)
        {
          target: wdt:P780 ?symptom .
          ?disease wdt:P780 ?symptom .
          FILTER (target: != ?disease)
          ?symptom rdfs:label ?symptom_label . FILTER(lang(?symptom_label) = "en")
        }
        GROUP BY ?disease
      }

      # Aggregate count
      BIND((COALESCE(?symptom_count, 0) + COALESCE(?gene_count, 0)) AS ?count)

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?count)
    '''

    sparql.setQuery(query_migraine)
    sparql.setReturnFormat(JSON)
    results_migraine = sparql.query().convert()

    reformatted_dict_migraine = {}

    entities_migraine = []
    result_list_migraine = results_migraine['results']['bindings']
    for res in result_list_migraine:
        for res_key, res_value in res.items():
            if res_key == 'disease':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                entities_migraine.append(entity_id)
                reformatted_dict_migraine[entity_id] = res

    df_migraine = pd.DataFrame.from_dict(reformatted_dict_migraine)
    df_migraine = df_migraine.transpose()

    df_migraine = df_migraine.apply(lambda x: x.apply(lambda y: y['value'] if type(y) == dict else y))

    for index, row in df_migraine.iterrows():
        if isinstance(row['symptoms'], str):
            row['symptoms'] = row['symptoms'].split(' // ')
    migraine_symptoms_count = df_migraine.symptom_count.value_counts()

    fig = px.histogram(migraine_symptoms_count, y=migraine_symptoms_count.values, x=migraine_symptoms_count.index)
    fig.update_layout(
        title="Migraine related disease number of symptoms",
        xaxis_title="Number of symptoms per related disease",
        yaxis_title="Number of diseases with x amount of symptoms",
        width=500)
    return fig


# Util functions for Bipolar Disorder: Q131755

# bar plot co-occuring topics

def co_occuring_topics():
    sparql_query = '''
    PREFIX target: <http://www.wikidata.org/entity/Q131755>

    SELECT ?count (CONCAT("/topics/{{ q }},", SUBSTR(STR(?topic), 32)) AS ?countUrl)
           ?topic ?topicLabel (CONCAT("/topic/", SUBSTR(STR(?topic), 32)) AS ?topicUrl)
           ?example_work ?example_workLabel (CONCAT("/work/", SUBSTR(STR(?example_work), 32)) AS ?example_workUrl)
    WITH {
      SELECT (COUNT(?work) AS ?count) ?topic (SAMPLE(?work) AS ?example_work) WHERE {
        # Find works for the specific queried topic
          ?work wdt:P921/( wdt:P31*/wdt:P279* | wdt:P361+ | wdt:P1269+) target: .

        # Find co-occuring topics
        ?work wdt:P921 ?topic .

        # Avoid listing the queried topic
          FILTER (target: != ?topic)
      }
      GROUP BY ?topic
    } AS %result
    WHERE {
      # Label the results
      INCLUDE %result
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh" . }
    }
    ORDER BY DESC(?count)
    '''

    # Set the query and format to JSON
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)

    # Execute the query and convert the results to a Pandas DataFrame
    results = sparql.query().convert()
    df = pd.json_normalize(results["results"]["bindings"])
    df["count.value"] = pd.to_numeric(df["count.value"])

    # filter the most relevant results
    df_filtered = df[df['count.value'] > 100]

    if not df_filtered.empty:
        fig = px.bar(df_filtered, y='topicLabel.value', x='count.value').update_layout(
            title='Publication Count by Co-Occurring Topics',
            xaxis=dict(title='Count'),
            yaxis=dict(title='Topic'))
        return fig


# Map: co-occuring topics

def create_map():
    query = '''
    PREFIX target: <http://www.wikidata.org/entity/Q131755>

    SELECT
      ?location ?locationLabel
      ?geo
      ?example_work ?example_workLabel
      ?latitude ?longitude
    WITH {
      SELECT
        ?location ?geo ?latitude ?longitude
        (SAMPLE(?work) AS ?example_work)
      WHERE {
        # Find works that are marked with the main subject of the topic.
        ?work wdt:P921 / ( wdt:P31*/wdt:P279* | wdt:P361+ | wdt:P1269+ ) target: .

        # Identify co-occurring topics that are geo-locatable.
        ?work wdt:P921 ?location .
        ?location wdt:P625 ?geo .
        BIND(xsd:float(STRAFTER(str(?geo), "Point(")) AS ?latitude) .
        BIND(xsd:float(STRAFTER(str(?geo), " ")) AS ?longitude) .
      }
      GROUP BY ?location ?geo ?latitude ?longitude
    } AS %results
    WHERE {
      INCLUDE %results

      # Label the results
      SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh".
      }
    }
    '''

    # Set the query and format to JSON
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Execute the query and convert the results to a Pandas DataFrame
    results = sparql.query().convert()
    df = pd.json_normalize(results["results"]["bindings"])

    # Extract the latitude and longitude values using regular expressions
    df["lat"] = df["geo.value"].str.extract(r"[\d.-]+\s+([\d.-]+)")
    df["lon"] = df["geo.value"].str.extract(r"([\d.-]+)\s+[\d.-]+")

    # Convert the extracted values to numeric
    df[["lat", "lon"]] = df[["lat", "lon"]].apply(pd.to_numeric)

    # Create the map figure using Plotly
    fig = go.Figure(
        go.Scattermapbox(
            lat=df["lat"],
            lon=df["lon"],
            mode="markers",
            marker=dict(size=5, color="blue"),
            text=df["locationLabel.value"],
            hoverinfo="text"
        )
    )

    fig.update_layout(
        mapbox=dict(
            accesstoken="pk.eyJ1IjoibHNjaHJldHQiLCJhIjoiY2xpaXRmMjUyMDFqODNjbHI1MG1ycnZndyJ9.TXJ8UKEEkreBV1QyPnbnqA",
            # Replace with your Mapbox access token
            center=dict(lat=0, lon=0),  # Set the initial center of the map
            zoom=0.5,  # Set the initial zoom level
        ),
        title="Map Visualization",
    )

    return fig


# bar plot: Publications about bipolar disorder per year
def publications_per_year():
    # Define SPARQL query
    query = f"""
    PREFIX target: <http://www.wikidata.org/entity/Q131755>

    # Inspired from LEGOLAS - http://abel.lis.illinois.edu/legolas/
    # Shubhanshu Mishra, Vetle Torvik
    select ?year (count(?work) as ?number_of_publications) where {{
      {{
        select (str(?year_) as ?year) (0 as ?pages) where {{
          # default values = 0
          ?year_item wdt:P31 wd:Q577 .
          ?year_item wdt:P585 ?date .
          bind(year(?date) as ?year_)
          {{
            select (min(?year_) as ?earliest_year) where {{
              {{ ?work wdt:P921/wdt:P31*/wdt:P279* target: . }}
              union {{ ?work wdt:P921/wdt:P361+ target: . }}
              union {{ ?work wdt:P921/wdt:P1269+ target: . }}
              ?work wdt:P577 ?publication_date .
              bind(year(?publication_date) as ?year_)
            }}
          }}
          bind(year(now()) as ?next_year)
          filter (?year_ >= ?earliest_year && ?year_ <= ?next_year)
        }}
      }}
      union {{
        select ?work (min(?years) as ?year) where {{
          {{ ?work wdt:P921/wdt:P31*/wdt:P279* target: . }}
          union {{ ?work wdt:P921/wdt:P361+ target: . }}
          union {{ ?work wdt:P921/wdt:P1269+ target: . }}
          ?work wdt:P577 ?dates .
          bind(str(year(?dates)) as ?years) .
        }}
        group by ?work
      }}
    }}
    group by ?year
    order by ?year
    """

    # Set the query and format to JSON
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Execute the query and convert the results to a Pandas DataFrame
    results = sparql.query().convert()
    df = pd.json_normalize(results["results"]["bindings"])
    df["year.value"] = pd.to_numeric(df["year.value"])
    df["number_of_publications.value"] = pd.to_numeric(df["number_of_publications.value"])

    # Create the bar chart using Plotly
    fig = px.bar(df, x="year.value", y="number_of_publications.value").update_layout(
        title='Publications per year',
        yaxis=dict(title='Count'),
        xaxis=dict(title='Year'))

    return fig


# Util function: Schizophrenia

def publications_per_year_schizophrenia():
    query = f"""
    PREFIX target: <http://www.wikidata.org/entity/Q41112>

    # Inspired from LEGOLAS - http://abel.lis.illinois.edu/legolas/
    # Shubhanshu Mishra, Vetle Torvik
    select ?year (count(?work) as ?number_of_publications) where {{
      {{
        select (str(?year_) as ?year) (0 as ?pages) where {{
          # default values = 0
          ?year_item wdt:P31 wd:Q577 .
          ?year_item wdt:P585 ?date .
          bind(year(?date) as ?year_)
          {{
            select (min(?year_) as ?earliest_year) where {{
              {{ ?work wdt:P921/wdt:P31*/wdt:P279* target: . }}
              union {{ ?work wdt:P921/wdt:P361+ target: . }}
              union {{ ?work wdt:P921/wdt:P1269+ target: . }}
              ?work wdt:P577 ?publication_date .
              bind(year(?publication_date) as ?year_)
            }}
          }}
          bind(year(now()) as ?next_year)
          filter (?year_ >= ?earliest_year && ?year_ <= ?next_year)
        }}
      }}
      union {{
        select ?work (min(?years) as ?year) where {{
          {{ ?work wdt:P921/wdt:P31*/wdt:P279* target: . }}
          union {{ ?work wdt:P921/wdt:P361+ target: . }}
          union {{ ?work wdt:P921/wdt:P1269+ target: . }}
          ?work wdt:P577 ?dates .
          bind(str(year(?dates)) as ?years) .
        }}
        group by ?work
      }}
    }}
    group by ?year
    order by ?year
    """

    # Set the query and format to JSON
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Execute the query and convert the results to a Pandas DataFrame
    results = sparql.query().convert()
    df = pd.json_normalize(results["results"]["bindings"])
    df["year.value"] = pd.to_numeric(df["year.value"])
    df["number_of_publications.value"] = pd.to_numeric(df["number_of_publications.value"])

    # Create the bar chart using Plotly
    fig = px.bar(df, x="year.value", y="number_of_publications.value").update_layout(
        title='Publications per year',
        yaxis=dict(title='Count'),
        xaxis=dict(title='Year'))

    return fig


# clinical trial per year
def clinical_trials_per_year():
    query = '''
    PREFIX target: <http://www.wikidata.org/entity/Q41112>

    SELECT
      DISTINCT
      ?start_date
      ?trial ?trialLabel
      ?intervention ?interventionLabel
      ?sponsor ?sponsorLabel
    WHERE {
      ?trial wdt:P31 wd:Q30612 ;
      wdt:P1050 / wdt:P279* target: .
      OPTIONAL {
        ?trial wdt:P580 ?starttime
        BIND(SUBSTR(STR(?starttime), 0, 11) AS ?start_date)
      }
      OPTIONAL { ?trial wdt:P4844 ?intervention }
      OPTIONAL { ?trial wdt:P859 ?sponsor }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,pl,ru,sv,zh". }
    }
    ORDER BY DESC(?starttime)
    '''
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # data preprocessing
    dict_trials = {}

    trials = []
    result_list = results['results']['bindings']
    for res in result_list:
        for res_key, res_value in res.items():
            if res_key == 'trial':
                uri = res_value['value']
                splitted_uri = uri.split('/')
                entity_id = splitted_uri[-1]
                trials.append(entity_id)
                dict_trials[entity_id] = res


    trial_df = pd.DataFrame.from_dict(dict_trials)
    trial_df = trial_df.transpose()
    years = []
    start_dates = []
    for index, row in trial_df.iterrows():
        start_date = row['start_date']
        if isinstance(start_date, dict) :
            value = start_date['value']
            start_dates.append(value)
    for date in start_dates:
        year = date[0:4]
        years.append(year)
    year_counts = {}
    for year in sorted(years):
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1

    year_counts_list = [(year, year_counts[year]) for year in year_counts]

    # group the data by year
    data_by_year = {}
    for year, value in year_counts_list:
        if year in data_by_year:
            data_by_year[year].append(value)
        else:
            data_by_year[year] = [value]

    # get the years and the values
    years = list(data_by_year.keys())
    values = [sum(data_by_year[year]) for year in years]

    # create the plot
    fig = go.Figure(data=[go.Bar(x=years, y=values)])
    fig.update_layout(
        title="Clinical Trials per Year",
        xaxis_title="Years",
        yaxis_title="Number of Trials",
        xaxis=dict(tickangle=90),
    )

    return fig
