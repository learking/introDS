--create view Freq2 as 
--SELECT * FROM Frequency
--UNION
--SELECT 'q' as docid, 'washington' as term, 1 as count 
--UNION
--SELECT 'q' as docid, 'taxes' as term, 1 as count
--UNION 
--SELECT 'q' as docid, 'treasury' as term, 1 as count;

create view ResultTab2 as
SELECT A.docid as fDoc, B.docid as sDoc, SUM(A.count * B.count) as sumCount
  FROM Freq2 A, Freq2 B
 WHERE A.term = B.term and A.docid < B.docid and (A.docid = 'q' or B.docid = 'q')
 GROUP BY A.docid, B.docid;

select fDoc, sDoc, max(sumCount) from ResultTab2;