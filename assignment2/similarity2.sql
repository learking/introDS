CREATE view FreqSubset AS
SELECT *
FROM Frequency
WHERE docid in ('10080_txt_crude','17035_txt_earn');

SELECT FrequencyA.docid, FrequencyB.docid, SUM(FrequencyA.count * FrequencyB.count)
FROM FreqSubset FrequencyA, FreqSubset FrequencyB
WHERE FrequencyA.term = FrequencyB.term
GROUP BY FrequencyA.docid, FrequencyB.docid;