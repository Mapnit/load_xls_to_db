USE [HenryRes]
GO

DROP TABLE [dbo].[Completion_Summary]
GO

CREATE TABLE [dbo].[Completion_Summary] (
    [Well_Name]    VARCHAR (50) NOT NULL,
    [Stage_Number] INT          NOT NULL,
    [Heel_Cluster] INT          NOT NULL,
    [Toe_Cluster]  INT          NOT NULL,
    [CF_Vol_gals]  INT          NOT NULL,
    [Total_BLTR]   INT          NOT NULL,
    [Prop_Cum_lbs] INT          NOT NULL,
    [Mesh_100]     INT          NOT NULL,
    [White_30_50]  INT 			NULL,
    [White_40_70]  INT 			NULL,
    [Proppant_3]   INT          NOT NULL,
    [Proppant_4]   INT          NOT NULL,
    [Open_Press]   INT          NOT NULL,
    [Fm_BD_Press]  INT          NOT NULL,
    [ISIP]         INT          NOT NULL,
    [Frac_Grad]    FLOAT	    NOT NULL,
    [Max_Rate]     INT          NOT NULL,
    [Avg_Rate]     FLOAT		NOT NULL,
    [Max_Press]    INT          NOT NULL,
    [Avg_Press]    FLOAT		NOT NULL,
	PRIMARY KEY ([Well_Name] ASC, [Stage_Number] ASC)
);


DROP TABLE [dbo].[Deviation_Survey]
GO

CREATE TABLE [dbo].[Deviation_Survey] (
    [Well_Name]    VARCHAR (50) NOT NULL,
    [MD] 		   INT          NOT NULL,
    [Angle] 	   FLOAT        NOT NULL,
    [Azimuth]  	   FLOAT        NOT NULL,
    [TVD]  		   FLOAT        NOT NULL,
    [Delta_NS]     FLOAT        NOT NULL,
    [Delta_EW] 	   FLOAT        NOT NULL,
    [Closure_D]    FLOAT        NOT NULL,
    [Closure_A]    FLOAT 		NOT NULL
	PRIMARY KEY ([Well_Name] ASC, [MD] ASC)
);


