import streamlit as st
import plotly.express as px
from PIL import Image


def run():
    st.title('Eksploratory Data Analysis')
    st.markdown('---')
    st.subheader('Faktor-faktor apa yang paling berkontribusi terhadap ketidakmampuan bayar pinjaman?')
    
    # gambar
    def load_and_display_images(start, end):
        for i in range(start, end+1):
            image = Image.open(f'{i}.png')
            st.image(image)
    
    load_and_display_images(1, 11)

    st.write('Dari visualisasi yang ada, dapat disimpulkan bahwa debitur yang memiliki bad loan adalah debitur yang termnya 36 bulan, durasi kerjanya lebih dari 10 tahun, kepemilikan rumahnya rent dan mortgage, purposenya untuk debt consolidation, statenya berada di CA.')


    # Membuat pembatas
    st.markdown('---')
    st.subheader('Analisis Kelompok Berisiko Tinggi')


    st.markdown('')
    st.markdown('*Statistical Analysis Profile non-risk (Fully Paid and Current)*')
    # Tabel HTML
    table_html_non_risk = """
        <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
        <tr style="text-align: right;">
        <th></th>
        <th>count</th>
        <th>mean</th>
        <th>min</th>
        <th>25%</th>
        <th>50%</th>
        <th>75%</th>
        <th>max</th>
        <th>std</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <th>member_id</th>
        <td>408965</td>
        <td>15023977</td>
        <td>70699</td>
        <td>4848490</td>
        <td>12326727</td>
        <td>23493526</td>
        <td>40860827</td>
        <td>11743058</td>
        </tr>
        <tr>
        <th>loan_amnt</th>
        <td>408965</td>
        <td>14291</td>
        <td>500</td>
        <td>8000</td>
        <td>12000</td>
        <td>20000</td>
        <td>35000</td>
        <td>8269</td>
        </tr>
        <tr>
        <th>funded_amnt</th>
        <td>408965</td>
        <td>14268</td>
        <td>500</td>
        <td>8000</td>
        <td>12000</td>
        <td>20000</td>
        <td>35000</td>
        <td>8258</td>
        </tr>
        <tr>
        <th>funded_amnt_inv</th>
        <td>408965</td>
        <td>14220</td>
        <td>0</td>
        <td>8000</td>
        <td>12000</td>
        <td>19950</td>
        <td>35000</td>
        <td>8269</td>
        </tr>
        <tr>
        <th>int_rate</th>
        <td>408965</td>
        <td>14</td>
        <td>5</td>
        <td>10</td>
        <td>13</td>
        <td>16</td>
        <td>26</td>
        <td>4</td>
        </tr>
        <tr>
        <th>installment</th>
        <td>408965</td>
        <td>431</td>
        <td>16</td>
        <td>255</td>
        <td>378</td>
        <td>565</td>
        <td>1410</td>
        <td>243</td>
        </tr>
        <tr>
        <th>annual_inc</th>
        <td>408965</td>
        <td>74255</td>
        <td>3000</td>
        <td>45000</td>
        <td>64000</td>
        <td>90000</td>
        <td>7500000</td>
        <td>56332</td>
        </tr>
        <tr>
        <th>issue_d</th>
        <td>408965</td>
        <td>1900-07-17 12:46:57.958504448</td>
        <td>1900-01-08 00:00:00</td>
        <td>1900-04-14 00:00:00</td>
        <td>1900-07-14 00:00:00</td>
        <td>1900-10-14 00:00:00</td>
        <td>1900-12-14 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>dti</th>
        <td>408965</td>
        <td>17</td>
        <td>0</td>
        <td>11</td>
        <td>17</td>
        <td>23</td>
        <td>40</td>
        <td>8</td>
        </tr>
        <tr>
        <th>delinq_2yrs</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>29</td>
        <td>1</td>
        </tr>
        <tr>
        <th>earliest_cr_line</th>
        <td>408965</td>
        <td>1997-11-11 03:18:11.685596800</td>
        <td>1969-01-01 00:00:00</td>
        <td>1994-02-01 00:00:00</td>
        <td>1999-02-01 00:00:00</td>
        <td>2002-08-01 00:00:00</td>
        <td>2068-12-01 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>inq_last_6mths</th>
        <td>408965</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>8</td>
        <td>1</td>
        </tr>
        <tr>
        <th>mths_since_last_delinq</th>
        <td>189173</td>
        <td>34</td>
        <td>0</td>
        <td>16</td>
        <td>31</td>
        <td>50</td>
        <td>188</td>
        <td>22</td>
        </tr>
        <tr>
        <th>mths_since_last_record</th>
        <td>54763</td>
        <td>75</td>
        <td>0</td>
        <td>53</td>
        <td>76</td>
        <td>102</td>
        <td>121</td>
        <td>30</td>
        </tr>
        <tr>
        <th>open_acc</th>
        <td>408965</td>
        <td>11</td>
        <td>0</td>
        <td>8</td>
        <td>10</td>
        <td>14</td>
        <td>84</td>
        <td>5</td>
        </tr>
        <tr>
        <th>pub_rec</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>63</td>
        <td>1</td>
        </tr>
        <tr>
        <th>revol_bal</th>
        <td>408965</td>
        <td>16318</td>
        <td>0</td>
        <td>6450</td>
        <td>11839</td>
        <td>20488</td>
        <td>2568995</td>
        <td>20559</td>
        </tr>
        <tr>
        <th>revol_util</th>
        <td>408720</td>
        <td>56</td>
        <td>0</td>
        <td>39</td>
        <td>57</td>
        <td>74</td>
        <td>892</td>
        <td>24</td>
        </tr>
        <tr>
        <th>total_acc</th>
        <td>408965</td>
        <td>25</td>
        <td>2</td>
        <td>17</td>
        <td>24</td>
        <td>32</td>
        <td>156</td>
        <td>12</td>
        </tr>
        <tr>
        <th>out_prncp</th>
        <td>408965</td>
        <td>4737</td>
        <td>0</td>
        <td>0</td>
        <td>1554</td>
        <td>7981</td>
        <td>31085</td>
        <td>6441</td>
        </tr>
        <tr>
        <th>out_prncp_inv</th>
        <td>408965</td>
        <td>4735</td>
        <td>0</td>
        <td>0</td>
        <td>1553</td>
        <td>7975</td>
        <td>31069</td>
        <td>6439</td>
        </tr>
        <tr>
        <th>total_pymnt</th>
        <td>408965</td>
        <td>12129</td>
        <td>394</td>
        <td>6006</td>
        <td>10060</td>
        <td>16047</td>
        <td>57778</td>
        <td>8378</td>
        </tr>
        <tr>
        <th>total_pymnt_inv</th>
        <td>408965</td>
        <td>12072</td>
        <td>0</td>
        <td>5969</td>
        <td>10003</td>
        <td>15980</td>
        <td>57778</td>
        <td>8361</td>
        </tr>
        <tr>
        <th>total_rec_prncp</th>
        <td>408965</td>
        <td>9526</td>
        <td>274</td>
        <td>4227</td>
        <td>7500</td>
        <td>12500</td>
        <td>35000</td>
        <td>7119</td>
        </tr>
        <tr>
        <th>total_rec_int</th>
        <td>408965</td>
        <td>2603</td>
        <td>0</td>
        <td>973</td>
        <td>1835</td>
        <td>3316</td>
        <td>24206</td>
        <td>2484</td>
        </tr>
        <tr>
        <th>total_rec_late_fee</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>287</td>
        <td>4</td>
        </tr>
        <tr>
        <th>recoveries</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        </tr>
        <tr>
        <th>collection_recovery_fee</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        </tr>
        <tr>
        <th>last_pymnt_d</th>
        <td>408965</td>
        <td>1900-05-14 17:32:58.593767680</td>
        <td>1900-01-08 00:00:00</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-03-14 00:00:00</td>
        <td>1900-09-15 00:00:00</td>
        <td>1900-12-15 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>last_pymnt_amnt</th>
        <td>408965</td>
        <td>3488</td>
        <td>0</td>
        <td>323</td>
        <td>590</td>
        <td>4353</td>
        <td>36234</td>
        <td>5828</td>
        </tr>
        <tr>
        <th>next_pymnt_d</th>
        <td>224226</td>
        <td>1900-02-12 07:26:41.701854720</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-03-16 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>last_credit_pull_d</th>
        <td>408931</td>
        <td>1900-03-10 00:04:09.102170880</td>
        <td>1900-01-08 00:00:00</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-02-15 00:00:00</td>
        <td>1900-12-15 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>collections_12_mths_ex_med</th>
        <td>408915</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>20</td>
        <td>0</td>
        </tr>
        <tr>
        <th>mths_since_last_major_derog</th>
        <td>87620</td>
        <td>43</td>
        <td>0</td>
        <td>26</td>
        <td>42</td>
        <td>59</td>
        <td>188</td>
        <td>22</td>
        </tr>
        <tr>
        <th>policy_code</th>
        <td>408965</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        </tr>
        <tr>
        <th>acc_now_delinq</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>5</td>
        <td>0</td>
        </tr>
        <tr>
        <th>tot_coll_amt</th>
        <td>351689</td>
        <td>198</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>9152545</td>
        <td>15516</td>
        </tr>
        <tr>
        <th>tot_cur_bal</th>
        <td>351689</td>
        <td>141540</td>
        <td>0</td>
        <td>29026</td>
        <td>85022</td>
        <td>213258</td>
        <td>8000078</td>
        <td>154297</td>
        </tr>
        <tr>
        <th>total_rev_hi_lim</th>
        <td>351689</td>
        <td>30901</td>
        <td>0</td>
        <td>13700</td>
        <td>23200</td>
        <td>38500</td>
        <td>9999999</td>
        <td>38477</td>
        </tr>
        <tr>
        <th>loan_category</th>
        <td>408965</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        </tr>
    </tbody>
    </table>
    </div>
    """

    # Memasukkan tabel HTML ke Streamlit
    st.markdown(table_html_non_risk, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')

    st.markdown('*Statistical Analysis Profile high-risk (Charged Off, Default)*')
    
    # Tabel HTML
    table_html_high_risk = """
    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
        <tr style="text-align: right;">
        <th></th>
        <th>count</th>
        <th>mean</th>
        <th>min</th>
        <th>25%</th>
        <th>50%</th>
        <th>75%</th>
        <th>max</th>
        <th>std</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <th>member_id</th>
        <td>43307</td>
        <td>10279642</td>
        <td>80353</td>
        <td>1784816</td>
        <td>7432069</td>
        <td>14907630</td>
        <td>40603904</td>
        <td>9846251</td>
        </tr>
        <tr>
        <th>loan_amnt</th>
        <td>43307</td>
        <td>14533</td>
        <td>900</td>
        <td>8000</td>
        <td>12600</td>
        <td>20000</td>
        <td>35000</td>
        <td>8373</td>
        </tr>
        <tr>
        <th>funded_amnt</th>
        <td>43307</td>
        <td>14486</td>
        <td>900</td>
        <td>8000</td>
        <td>12550</td>
        <td>20000</td>
        <td>35000</td>
        <td>8345</td>
        </tr>
        <tr>
        <th>funded_amnt_inv</th>
        <td>43307</td>
        <td>14360</td>
        <td>0</td>
        <td>8000</td>
        <td>12300</td>
        <td>19950</td>
        <td>35000</td>
        <td>8371</td>
        </tr>
        <tr>
        <th>int_rate</th>
        <td>43307</td>
        <td>16</td>
        <td>5</td>
        <td>13</td>
        <td>16</td>
        <td>19</td>
        <td>26</td>
        <td>4</td>
        </tr>
        <tr>
        <th>installment</th>
        <td>43307</td>
        <td>440</td>
        <td>22</td>
        <td>265</td>
        <td>391</td>
        <td>573</td>
        <td>1408</td>
        <td>246</td>
        </tr>
        <tr>
        <th>annual_inc</th>
        <td>43307</td>
        <td>64767</td>
        <td>4080</td>
        <td>40000</td>
        <td>56000</td>
        <td>78000</td>
        <td>932000</td>
        <td>39957</td>
        </tr>
        <tr>
        <th>issue_d</th>
        <td>43307</td>
        <td>1900-07-05 06:16:53.988500736</td>
        <td>1900-01-08 00:00:00</td>
        <td>1900-04-13 00:00:00</td>
        <td>1900-07-13 00:00:00</td>
        <td>1900-10-12 00:00:00</td>
        <td>1900-12-14 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>dti</th>
        <td>43307</td>
        <td>18</td>
        <td>0</td>
        <td>12</td>
        <td>18</td>
        <td>24</td>
        <td>40</td>
        <td>8</td>
        </tr>
        <tr>
        <th>delinq_2yrs</th>
        <td>43307</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>18</td>
        <td>1</td>
        </tr>
        <tr>
        <th>earliest_cr_line</th>
        <td>43307</td>
        <td>1998-09-25 15:20:07.259796352</td>
        <td>1969-01-01 00:00:00</td>
        <td>1995-04-01 00:00:00</td>
        <td>1999-10-01 00:00:00</td>
        <td>2003-03-01 00:00:00</td>
        <td>2068-11-01 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>inq_last_6mths</th>
        <td>43307</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>8</td>
        <td>1</td>
        </tr>
        <tr>
        <th>mths_since_last_delinq</th>
        <td>19226</td>
        <td>34</td>
        <td>0</td>
        <td>15</td>
        <td>31</td>
        <td>50</td>
        <td>152</td>
        <td>22</td>
        </tr>
        <tr>
        <th>mths_since_last_record</th>
        <td>5262</td>
        <td>79</td>
        <td>0</td>
        <td>59</td>
        <td>87</td>
        <td>104</td>
        <td>129</td>
        <td>30</td>
        </tr>
        <tr>
        <th>open_acc</th>
        <td>43307</td>
        <td>11</td>
        <td>0</td>
        <td>8</td>
        <td>10</td>
        <td>14</td>
        <td>76</td>
        <td>5</td>
        </tr>
        <tr>
        <th>pub_rec</th>
        <td>43307</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>9</td>
        <td>0</td>
        </tr>
        <tr>
        <th>revol_bal</th>
        <td>43307</td>
        <td>14914</td>
        <td>0</td>
        <td>6290</td>
        <td>11375</td>
        <td>19140</td>
        <td>1746716</td>
        <td>17046</td>
        </tr>
        <tr>
        <th>revol_util</th>
        <td>43260</td>
        <td>60</td>
        <td>0</td>
        <td>44</td>
        <td>62</td>
        <td>78</td>
        <td>129</td>
        <td>23</td>
        </tr>
        <tr>
        <th>total_acc</th>
        <td>43307</td>
        <td>24</td>
        <td>2</td>
        <td>16</td>
        <td>23</td>
        <td>31</td>
        <td>94</td>
        <td>11</td>
        </tr>
        <tr>
        <th>out_prncp</th>
        <td>43307</td>
        <td>202</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>32160</td>
        <td>1749</td>
        </tr>
        <tr>
        <th>out_prncp_inv</th>
        <td>43307</td>
        <td>202</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>32160</td>
        <td>1748</td>
        </tr>
        <tr>
        <th>total_pymnt</th>
        <td>43307</td>
        <td>6679</td>
        <td>0</td>
        <td>2798</td>
        <td>5180</td>
        <td>8965</td>
        <td>46199</td>
        <td>5457</td>
        </tr>
        <tr>
        <th>total_pymnt_inv</th>
        <td>43307</td>
        <td>6614</td>
        <td>0</td>
        <td>2749</td>
        <td>5125</td>
        <td>8901</td>
        <td>46163</td>
        <td>5436</td>
        </tr>
        <tr>
        <th>total_rec_prncp</th>
        <td>43307</td>
        <td>3509</td>
        <td>0</td>
        <td>1259</td>
        <td>2522</td>
        <td>4672</td>
        <td>34483</td>
        <td>3329</td>
        </tr>
        <tr>
        <th>total_rec_int</th>
        <td>43307</td>
        <td>2259</td>
        <td>0</td>
        <td>754</td>
        <td>1536</td>
        <td>2927</td>
        <td>20610</td>
        <td>2282</td>
        </tr>
        <tr>
        <th>total_rec_late_fee</th>
        <td>43307</td>
        <td>3</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>359</td>
        <td>10</td>
        </tr>
        <tr>
        <th>recoveries</th>
        <td>43307</td>
        <td>909</td>
        <td>0</td>
        <td>0</td>
        <td>114</td>
        <td>1298</td>
        <td>33520</td>
        <td>1572</td>
        </tr>
        <tr>
        <th>collection_recovery_fee</th>
        <td>43307</td>
        <td>94</td>
        <td>0</td>
        <td>0</td>
        <td>2</td>
        <td>28</td>
        <td>7002</td>
        <td>257</td>
        </tr>
        <tr>
        <th>last_pymnt_d</th>
        <td>42943</td>
        <td>1900-06-27 16:55:24.444030464</td>
        <td>1900-01-09 00:00:00</td>
        <td>1900-04-14 00:00:00</td>
        <td>1900-07-11 00:00:00</td>
        <td>1900-09-14 00:00:00</td>
        <td>1900-12-15 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>last_pymnt_amnt</th>
        <td>43307</td>
        <td>455</td>
        <td>0</td>
        <td>238</td>
        <td>377</td>
        <td>569</td>
        <td>34833</td>
        <td>624</td>
        </tr>
        <tr>
        <th>next_pymnt_d</th>
        <td>832</td>
        <td>1900-02-14 12:13:50.769230848</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>1900-02-16 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>last_credit_pull_d</th>
        <td>43301</td>
        <td>1900-04-27 09:30:06.027574528</td>
        <td>1900-01-09 00:00:00</td>
        <td>1900-01-16 00:00:00</td>
        <td>1900-02-15 00:00:00</td>
        <td>1900-08-14 00:00:00</td>
        <td>1900-12-15 00:00:00</td>
        <td>NaN</td>
        </tr>
        <tr>
        <th>collections_12_mths_ex_med</th>
        <td>43301</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>4</td>
        <td>0</td>
        </tr>
        <tr>
        <th>mths_since_last_major_derog</th>
        <td>8167</td>
        <td>43</td>
        <td>0</td>
        <td>25</td>
        <td>42</td>
        <td>60</td>
        <td>152</td>
        <td>22</td>
        </tr>
        <tr>
        <th>policy_code</th>
        <td>43307</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        </tr>
        <tr>
        <th>acc_now_delinq</th>
        <td>43307</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>5</td>
        <td>0</td>
        </tr>
        <tr>
        <th>tot_coll_amt</th>
        <td>33270</td>
        <td>127</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>95806</td>
        <td>1295</td>
        </tr>
        <tr>
        <th>tot_cur_bal</th>
        <td>33270</td>
        <td>114411</td>
        <td>0</td>
        <td>25434</td>
        <td>59704</td>
        <td>172947</td>
        <td>3437283</td>
        <td>127461</td>
        </tr>
        <tr>
        <th>total_rev_hi_lim</th>
        <td>33270</td>
        <td>26220</td>
        <td>0</td>
        <td>12500</td>
        <td>20500</td>
        <td>33100</td>
        <td>1998700</td>
        <td>25020</td>
        </tr>
        <tr>
        <th>loan_category</th>
        <td>43307</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        </tr>
    </tbody>
    </table>
    </div>
    """

    # Memasukkan tabel HTML ke Streamlit
    st.markdown(table_html_high_risk, unsafe_allow_html=True)

    st.markdown("### annual_inc")
    st.write("""
    **Insight:**
    
    - Debitur pada kategori "non-risk" memiliki rata-rata pendapatan yang lebih tinggi ($74,255) dibandingkan dengan debitur pada kategori "high risk" ($64,767).
    - Deviasi standar yang tinggi pada kedua kategori menunjukkan variasi yang cukup besar dalam pendapatan.
    
    **Rekomendasi Bisnis:**
    
    - Mungkin diperlukan peninjauan ulang terhadap kebijakan peminjaman untuk kategori "high risk" guna meminimalkan risiko gagal bayar.
    - Fokus pada pengembangan produk atau layanan yang lebih sesuai dengan profil dan kemampuan pembayaran debitur pada kategori "high risk".
    - Perlu dilakukan analisis lebih lanjut untuk memahami faktor-faktor lain yang dapat memberikan wawasan tambahan terkait risiko kredit.
    """)
    
    st.markdown("### dti")
    st.write("""
    **Insight:**
    
    - Debitur pada kategori "non-risk" memiliki rata-rata Debt-to-Income (DTI) yang lebih rendah (17) dibandingkan dengan debitur pada kategori "high risk" (18).
    - Meskipun rata-rata DTI berbeda, deviasi standar yang sama pada kedua kategori menunjukkan bahwa ada variasi yang cukup besar dalam DTI di setiap kategori.
    
    **Rekomendasi Bisnis:**
    
    - Pertimbangkan untuk menetapkan batasan DTI yang lebih ketat untuk kategori "high risk" guna meminimalkan risiko gagal bayar.
    - Melakukan pendekatan risiko khusus terhadap debitur pada kategori "high risk" dengan penilaian lebih cermat terhadap kemampuan mereka untuk melunasi pinjaman.
    - Lakukan pemantauan berkala terhadap debitur pada kedua kategori untuk mengidentifikasi perubahan dalam kondisi keuangan mereka.
    """)

    st.markdown("### revol_util")
    st.write("""
    **Insight:**
    
    - Penggunaan total kredit (revolving credit utilization) pada kategori "high risk" (60%) lebih tinggi dibandingkan dengan kategori "non-risk" (56%).
    - Tingkat penggunaan kredit yang tinggi dapat mengindikasikan tekanan keuangan pada debitur.
    
    **Rekomendasi Bisnis:**
    
    - Perlu dipertimbangkan pendekatan khusus dalam menilai risiko berdasarkan tingkat penggunaan kredit pada kategori "high risk".
    - Edukasi dan dukungan tambahan bagi debitur pada kategori "high risk" untuk manajemen keuangan yang lebih baik.
    - Implementasi strategi mitigasi risiko yang spesifik untuk mengatasi tingkat penggunaan kredit yang tinggi.
    """)
if __name__ == '__main__':
    run()