SELECT FrequencyA.docid, FrequencyB.term, SUM(FrequencyA.count * FrequencyB.count)
  FROM Frequency FrequencyA, Frequency FrequencyB
 WHERE FrequencyA.term = FrequencyB.term and FrequencyA.docid < FrequencyB.docid
 GROUP BY FrequencyA.docid, FrequencyB.term;