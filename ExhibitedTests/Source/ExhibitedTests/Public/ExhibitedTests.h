// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

// Log for unit tests outputs
DECLARE_LOG_CATEGORY_EXTERN(LogUnitTest, Log, All)

// Log for Unit tests debug prints
DECLARE_LOG_CATEGORY_EXTERN(LogUnitTestDebug, Log, All)

struct FAssetData;

class FExhibitedTestsModule : public IModuleInterface
{
public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
};
